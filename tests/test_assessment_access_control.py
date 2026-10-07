"""Access-control tests for the customer- and assessment-scoped API.

Assessment and customer ids are sequential integers, so every one of these
endpoints must reject both anonymous callers and authenticated callers who do
not own the record. Each endpoint is checked three ways: anonymous, wrong
tenant, and owner.
"""
import pytest


def assessment_endpoints(assessment_id):
    """(method, url) for every endpoint keyed on an assessment id."""
    return [
        ("GET", f"/api/assessments/{assessment_id}"),
        ("GET", f"/api/assessments/{assessment_id}/answers"),
        ("GET", f"/api/assessments/{assessment_id}/scores"),
        ("GET", f"/api/assessments/{assessment_id}/radar-data"),
        ("PUT", f"/api/assessments/{assessment_id}/complete"),
    ]


def customer_endpoints(customer_id):
    """(method, url) for every endpoint keyed on a customer id."""
    return [
        ("GET", f"/api/customers/{customer_id}"),
        ("GET", f"/api/customers/{customer_id}/assessments"),
        ("GET", f"/api/customers/{customer_id}/progress"),
    ]


def ids(cases):
    return [f"{method} {url}" for method, url in cases]


# --------------------------------------------------------------------------
# Anonymous callers
# --------------------------------------------------------------------------

@pytest.mark.parametrize(
    "method,url",
    assessment_endpoints(1) + customer_endpoints(1),
    ids=ids(assessment_endpoints(1) + customer_endpoints(1)),
)
def test_rejects_anonymous(client, alice, method, url):
    """No endpoint may serve data without credentials."""
    response = client.request(method, url)
    assert response.status_code in (401, 403), (
        f"{method} {url} served an anonymous caller with "
        f"{response.status_code}: {response.text[:200]}"
    )


def test_rejects_anonymous_answer_submission(client, alice, question):
    response = client.post(
        "/api/answers",
        json={
            "assessment_id": alice["assessment_id"],
            "question_id": question["question_id"],
            "answer_option_id": question["option_id"],
        },
    )
    assert response.status_code in (401, 403), response.text


# --------------------------------------------------------------------------
# Authenticated, but the wrong tenant
# --------------------------------------------------------------------------

def test_bob_cannot_read_alices_assessment(client, alice, bob):
    for method, url in assessment_endpoints(alice["assessment_id"]):
        response = client.request(method, url, headers=bob["headers"])
        assert response.status_code == 403, (
            f"{method} {url} leaked Alice's assessment to Bob with "
            f"{response.status_code}: {response.text[:200]}"
        )


def test_bob_cannot_read_alices_customer(client, alice, bob):
    for method, url in customer_endpoints(alice["customer_id"]):
        response = client.request(method, url, headers=bob["headers"])
        assert response.status_code == 403, (
            f"{method} {url} leaked Alice's customer to Bob with "
            f"{response.status_code}: {response.text[:200]}"
        )


def test_bob_cannot_write_into_alices_assessment(client, alice, bob, db, question):
    """The most damaging case: writing answers into another tenant's assessment."""
    response = client.post(
        "/api/answers",
        json={
            "assessment_id": alice["assessment_id"],
            "question_id": question["question_id"],
            "answer_option_id": question["option_id"],
        },
        headers=bob["headers"],
    )
    assert response.status_code == 403, response.text

    # And nothing was persisted.
    conn = db.get_connection()
    try:
        count = conn.execute(
            "SELECT COUNT(*) FROM assessment_answers WHERE assessment_id = ? AND question_id = ?",
            (alice["assessment_id"], question["question_id"]),
        ).fetchone()[0]
    finally:
        conn.close()
    assert count == 0, "Bob's rejected answer was written to Alice's assessment anyway"


def test_bob_cannot_complete_alices_assessment(client, alice, bob, db):
    response = client.put(
        f"/api/assessments/{alice['assessment_id']}/complete",
        headers=bob["headers"],
    )
    assert response.status_code == 403, response.text
    assert db.get_assessment(alice["assessment_id"])["status"] != "completed"


def test_bob_cannot_create_assessment_for_alices_customer(client, alice, bob):
    response = client.post(
        "/api/assessments",
        json={"customer_id": alice["customer_id"], "name": "intrusion"},
        headers=bob["headers"],
    )
    assert response.status_code == 403, response.text


def test_customer_listing_is_scoped_to_the_caller(client, alice, bob):
    response = client.get("/api/customers", headers=bob["headers"])
    assert response.status_code == 200, response.text
    returned = {c["id"] for c in response.json()["customers"]}
    assert alice["customer_id"] not in returned
    assert bob["customer_id"] in returned


# --------------------------------------------------------------------------
# The owner still has access (the guard is not simply denying everyone)
# --------------------------------------------------------------------------

def test_owner_can_read_own_assessment(client, alice):
    for method, url in assessment_endpoints(alice["assessment_id"]):
        if method == "PUT":
            continue  # completing it is covered separately; it mutates state
        response = client.request(method, url, headers=alice["headers"])
        assert response.status_code == 200, (
            f"{method} {url} denied the owner: "
            f"{response.status_code}: {response.text[:200]}"
        )


def test_owner_can_read_own_customer(client, alice):
    for method, url in customer_endpoints(alice["customer_id"]):
        response = client.request(method, url, headers=alice["headers"])
        assert response.status_code == 200, (
            f"{method} {url} denied the owner: "
            f"{response.status_code}: {response.text[:200]}"
        )


def test_owner_can_submit_and_read_back_an_answer(client, alice, question):
    response = client.post(
        "/api/answers",
        json={
            "assessment_id": alice["assessment_id"],
            "question_id": question["question_id"],
            "answer_option_id": question["option_id"],
            "answer_text": "evidence note",
        },
        headers=alice["headers"],
    )
    assert response.status_code == 200, response.text

    answers = client.get(
        f"/api/assessments/{alice['assessment_id']}/answers",
        headers=alice["headers"],
    )
    assert answers.status_code == 200, answers.text
    stored = {a["question_id"] for a in answers.json()["answers"]}
    assert question["question_id"] in stored


def test_unknown_answer_option_is_a_client_error(client, alice, question):
    """An invalid option id must be a 400, not an unhandled 500."""
    response = client.post(
        "/api/answers",
        json={
            "assessment_id": alice["assessment_id"],
            "question_id": question["question_id"],
            "answer_option_id": 10_000_000,
        },
        headers=alice["headers"],
    )
    assert response.status_code == 400, response.text


# --------------------------------------------------------------------------
# Missing records must not reveal themselves differently
# --------------------------------------------------------------------------

def test_absent_assessment_is_not_found_for_authenticated_caller(client, alice):
    response = client.get("/api/assessments/9999999", headers=alice["headers"])
    assert response.status_code == 404, response.text
