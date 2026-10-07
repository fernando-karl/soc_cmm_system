"""Shared fixtures for the automated test suite.

The application reads its database location and signing key from the
environment at import time, so both are set here — before `main`, `auth` or
`database` are imported anywhere — and point at a throwaway SQLite file.
"""
import os
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

# Must happen before the application modules are imported.
_TMP_DIR = tempfile.mkdtemp(prefix="soc-cmm-tests-")
os.environ["DB_PATH"] = str(Path(_TMP_DIR) / "test.db")
os.environ.setdefault("SECRET_KEY", "test-only-secret-key-not-for-production")

import pytest  # noqa: E402
from starlette.testclient import TestClient  # noqa: E402

import database  # noqa: E402
from auth import auth_manager  # noqa: E402

SCHEMA_EXTRAS = [
    REPO_ROOT / "sql" / "schema" / "bilingual_schema.sql",
    REPO_ROOT / "sql" / "migrations" / "add_admin_field.sql",
]


def _build_schema(db: database.DatabaseManager) -> None:
    """Create the schema and apply the migrations the application expects."""
    db.init_database()
    conn = db.get_connection()
    try:
        for extra in SCHEMA_EXTRAS:
            conn.executescript(extra.read_text(encoding="utf-8"))
        conn.commit()
    finally:
        conn.close()


@pytest.fixture(scope="session")
def db():
    """A fresh, seeded database shared by the whole session."""
    manager = database.DatabaseManager()
    _build_schema(manager)
    manager.populate_initial_data()
    return manager


@pytest.fixture(scope="session")
def client(db):
    """TestClient bound to the application, with the database already built."""
    import main
    return TestClient(main.app)


def _make_user(username: str, password: str) -> dict:
    user_id = auth_manager.create_user(
        username=username,
        email=f"{username}@tests.invalid",
        password=password,
        full_name=username.title(),
    )
    return {"id": user_id, "username": username, "password": password}


def _login(client: TestClient, user: dict) -> str:
    response = client.post(
        "/api/auth/login",
        json={"username": user["username"], "password": user["password"]},
    )
    assert response.status_code == 200, response.text
    token = response.json()["access_token"]
    # Logging in also sets a session cookie. The shared TestClient would then
    # carry it into every later request, including the ones that must be
    # anonymous, so drop it and authenticate explicitly via headers.
    client.cookies.clear()
    return token


def _tenant(client: TestClient, db, username: str) -> dict:
    """A user with one customer and one assessment, plus a bearer token."""
    user = _make_user(username, f"{username}-Pw!123")
    user["token"] = _login(client, user)
    user["headers"] = {"Authorization": f"Bearer {user['token']}"}
    user["customer_id"] = db.create_customer(
        user_id=user["id"], name=f"{username} Corp", email=f"{username}@corp.invalid"
    )
    user["assessment_id"] = db.create_assessment(
        customer_id=user["customer_id"], name=f"{username} assessment"
    )
    return user


@pytest.fixture(scope="session")
def alice(client, db):
    """Owner of the data the tests try to reach."""
    return _tenant(client, db, "alice")


@pytest.fixture(scope="session")
def bob(client, db):
    """A second, unrelated tenant — must never see Alice's data."""
    return _tenant(client, db, "bob")


@pytest.fixture(scope="session")
def question(db):
    """A real question id and one of its answer option ids."""
    conn = db.get_connection()
    try:
        row = conn.execute(
            "SELECT q.id AS question_id, o.id AS option_id "
            "FROM questions q JOIN answer_options o ON o.question_id = q.id LIMIT 1"
        ).fetchone()
    finally:
        conn.close()
    if row is None:
        import pytest as _pytest
        _pytest.skip("no seeded questions with answer options")
    return {"question_id": row["question_id"], "option_id": row["option_id"]}


@pytest.fixture(autouse=True)
def _no_ambient_credentials(client):
    """Guarantee each test starts with no cookie-based session.

    Every test authenticates with an explicit `Authorization` header, so a
    leftover cookie could silently turn an anonymous-access assertion into an
    authenticated request and hide a real hole.
    """
    client.cookies.clear()
    yield
    client.cookies.clear()
