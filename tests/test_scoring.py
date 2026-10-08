"""Scores must follow the official SOC-CMM® workbook, not a plain average.

The workbook's `_Output` sheet computes, per aspect, over answers `a` in 1..5
with importance factor `h`:

    total = SUM(a*h)   max = SUM(5*h)   min = SUM(h)
    percentage = 100 * (total - min) / (max - min)

The subtraction of `min` is the part that matters: it normalises over the range
of the scale, so the lowest answer scores 0%. The previous implementation used
`mean(a) / 5`, which gave that same answer 20%.
"""
import pytest

import database


def answers_for(db, assessment_id, aspect_id, level, importance=None):
    """Answer every question of one aspect at `level`."""
    conn = db.get_connection()
    try:
        question_ids = [r[0] for r in conn.execute(
            "SELECT id FROM questions WHERE aspect_id = ? ORDER BY id", (aspect_id,))]
    finally:
        conn.close()
    assert question_ids, f"aspect {aspect_id} has no questions"
    for question_id in question_ids:
        db.save_answer(assessment_id=assessment_id, question_id=question_id,
                       answer_option_id=option_at(db, question_id, level),
                       importance=importance)
    return question_ids


def option_at(db, question_id, level):
    conn = db.get_connection()
    try:
        row = conn.execute(
            "SELECT id FROM answer_options WHERE question_id = ? AND maturity_level = ?",
            (question_id, level)).fetchone()
    finally:
        conn.close()
    assert row is not None, f"question {question_id} has no option at level {level}"
    return row[0]


def aspect_percentage(db, assessment_id, aspect_id):
    conn = db.get_connection()
    try:
        row = conn.execute(
            "SELECT percentage, score FROM assessment_scores "
            "WHERE assessment_id = ? AND aspect_id = ?",
            (assessment_id, aspect_id)).fetchone()
    finally:
        conn.close()
    return (None, None) if row is None else (row[0], row[1])


@pytest.fixture
def scored(db, alice):
    """A fresh assessment of Alice's, plus the id of an aspect to score."""
    assessment_id = db.create_assessment(customer_id=alice["customer_id"],
                                         name="scoring fixture")
    conn = db.get_connection()
    try:
        aspect_id = conn.execute(
            "SELECT aspect_id FROM questions GROUP BY aspect_id "
            "HAVING COUNT(*) > 1 ORDER BY aspect_id LIMIT 1").fetchone()[0]
    finally:
        conn.close()
    return {"assessment_id": assessment_id, "aspect_id": aspect_id}


@pytest.mark.parametrize("level,expected", [
    (1, 0.0), (2, 25.0), (3, 50.0), (4, 75.0), (5, 100.0),
])
def test_a_uniform_answer_scores_what_the_workbook_scores(db, scored, level, expected):
    """100 * (a-1)/4 — in particular level 1 is 0%, where the old code gave 20%."""
    answers_for(db, scored["assessment_id"], scored["aspect_id"], level)
    db.calculate_assessment_scores(scored["assessment_id"])
    percentage, _ = aspect_percentage(db, scored["assessment_id"], scored["aspect_id"])
    assert percentage == pytest.approx(expected), (
        f"level {level} scored {percentage}%, the workbook gives {expected}%")


def test_the_lowest_answer_is_not_a_fifth_of_the_scale(db, scored):
    """The regression this change exists to fix: a non-existent SOC read 20%."""
    answers_for(db, scored["assessment_id"], scored["aspect_id"], 1)
    db.calculate_assessment_scores(scored["assessment_id"])
    percentage, score = aspect_percentage(db, scored["assessment_id"], scored["aspect_id"])
    assert percentage == 0.0
    assert score == 0.0


def test_maturity_is_reported_on_the_familiar_zero_to_five_scale(db, scored):
    answers_for(db, scored["assessment_id"], scored["aspect_id"], 3)
    db.calculate_assessment_scores(scored["assessment_id"])
    percentage, score = aspect_percentage(db, scored["assessment_id"], scored["aspect_id"])
    # The workbook's results sheet derives maturity as 5 * percentage / 100.
    assert score == pytest.approx(database.MATURITY_MAX * percentage / 100.0)
    assert score == pytest.approx(2.5)


def test_importance_weights_a_mixed_aspect(db, alice):
    """With two questions answered 1 and 5, weighting moves the result.

    Equal importance gives the midpoint. Making the high answer `critical`
    (factor 4) against the low answer's `low` (factor 0.5) pulls it up.
    """
    conn = db.get_connection()
    try:
        row = conn.execute(
            "SELECT aspect_id, COUNT(*) n FROM questions GROUP BY aspect_id "
            "HAVING n >= 2 ORDER BY aspect_id LIMIT 1").fetchone()
        aspect_id = row[0]
        q_low, q_high = [r[0] for r in conn.execute(
            "SELECT id FROM questions WHERE aspect_id = ? ORDER BY id LIMIT 2",
            (aspect_id,))]
    finally:
        conn.close()

    def run(importance_low, importance_high):
        assessment_id = db.create_assessment(customer_id=alice["customer_id"],
                                             name="weighting")
        db.save_answer(assessment_id, q_low, option_at(db, q_low, 1),
                       importance=importance_low)
        db.save_answer(assessment_id, q_high, option_at(db, q_high, 5),
                       importance=importance_high)
        # Only these two are answered, and scoring counts answered questions.
        db.calculate_assessment_scores(assessment_id)
        return aspect_percentage(db, assessment_id, aspect_id)[0]

    equal = run(3, 3)
    assert equal == pytest.approx(50.0), f"equal importance gave {equal}%"

    weighted_up = run(2, 5)      # low importance on the 1, critical on the 5
    assert weighted_up > equal, f"{weighted_up}% should exceed {equal}%"
    # 100 * (0.5*0 + 4*1) / (0.5 + 4) = 88.88..
    assert weighted_up == pytest.approx(100 * 4 / 4.5, abs=0.01)

    weighted_down = run(5, 2)
    assert weighted_down < equal, f"{weighted_down}% should be below {equal}%"


def test_importance_none_drops_a_question_out_of_the_score(db, alice):
    """Factor 0 — the workbook's `none` removes the question from the score."""
    conn = db.get_connection()
    try:
        aspect_id = conn.execute(
            "SELECT aspect_id FROM questions GROUP BY aspect_id "
            "HAVING COUNT(*) >= 2 ORDER BY aspect_id LIMIT 1").fetchone()[0]
        q_a, q_b = [r[0] for r in conn.execute(
            "SELECT id FROM questions WHERE aspect_id = ? ORDER BY id LIMIT 2",
            (aspect_id,))]
    finally:
        conn.close()

    assessment_id = db.create_assessment(customer_id=alice["customer_id"],
                                         name="none importance")
    db.save_answer(assessment_id, q_a, option_at(db, q_a, 5), importance=3)
    db.save_answer(assessment_id, q_b, option_at(db, q_b, 1), importance=1)
    db.calculate_assessment_scores(assessment_id)
    percentage, _ = aspect_percentage(db, assessment_id, aspect_id)
    assert percentage == pytest.approx(100.0), (
        f"the `none` question still affected the score: {percentage}%")


def test_an_aspect_of_only_none_questions_gets_no_score(db, alice):
    """SUM(h) == 0 leaves the percentage undefined; store nothing rather than 0."""
    conn = db.get_connection()
    try:
        aspect_id = conn.execute(
            "SELECT aspect_id FROM questions GROUP BY aspect_id "
            "ORDER BY aspect_id LIMIT 1").fetchone()[0]
        question_id = conn.execute(
            "SELECT id FROM questions WHERE aspect_id = ? LIMIT 1",
            (aspect_id,)).fetchone()[0]
    finally:
        conn.close()
    assessment_id = db.create_assessment(customer_id=alice["customer_id"],
                                         name="all none")
    db.save_answer(assessment_id, question_id, option_at(db, question_id, 4),
                   importance=1)
    db.calculate_assessment_scores(assessment_id)
    percentage, _ = aspect_percentage(db, assessment_id, aspect_id)
    assert percentage is None


def test_importance_defaults_to_normal(db, alice):
    """Omitting it must behave exactly as the workbook's shipped default."""
    conn = db.get_connection()
    try:
        question_id = conn.execute("SELECT id FROM questions LIMIT 1").fetchone()[0]
    finally:
        conn.close()
    assessment_id = db.create_assessment(customer_id=alice["customer_id"],
                                         name="default importance")
    db.save_answer(assessment_id, question_id, option_at(db, question_id, 3))
    conn = db.get_connection()
    try:
        stored = conn.execute(
            "SELECT importance FROM assessment_answers WHERE assessment_id = ?",
            (assessment_id,)).fetchone()[0]
    finally:
        conn.close()
    assert stored == database.IMPORTANCE_NORMAL == 3


def test_an_unknown_importance_is_rejected(db, alice):
    conn = db.get_connection()
    try:
        question_id = conn.execute("SELECT id FROM questions LIMIT 1").fetchone()[0]
    finally:
        conn.close()
    assessment_id = db.create_assessment(customer_id=alice["customer_id"],
                                         name="bad importance")
    with pytest.raises(ValueError, match="importance"):
        db.save_answer(assessment_id, question_id,
                       option_at(db, question_id, 3), importance=9)


def test_the_domain_score_is_the_mean_of_its_aspects(db, alice):
    """The workbook's results sheet averages aspects, unweighted."""
    conn = db.get_connection()
    try:
        domain_id, aspect_ids = None, []
        for row in conn.execute(
                "SELECT domain_id, id FROM aspects ORDER BY domain_id, id"):
            if domain_id is None:
                domain_id = row[0]
            if row[0] == domain_id:
                aspect_ids.append(row[1])
        aspect_ids = aspect_ids[:2]
    finally:
        conn.close()
    assert len(aspect_ids) == 2

    assessment_id = db.create_assessment(customer_id=alice["customer_id"],
                                         name="domain mean")
    answers_for(db, assessment_id, aspect_ids[0], 1)   # 0%
    answers_for(db, assessment_id, aspect_ids[1], 5)   # 100%
    db.calculate_assessment_scores(assessment_id)

    conn = db.get_connection()
    try:
        domain_pct = conn.execute(
            "SELECT percentage FROM assessment_scores "
            "WHERE assessment_id = ? AND domain_id = ? AND aspect_id IS NULL",
            (assessment_id, domain_id)).fetchone()[0]
        aspect_pcts = [r[0] for r in conn.execute(
            "SELECT percentage FROM assessment_scores "
            "WHERE assessment_id = ? AND aspect_id IN (?, ?)",
            (assessment_id, *aspect_ids))]
    finally:
        conn.close()
    assert sorted(aspect_pcts) == [pytest.approx(0.0), pytest.approx(100.0)]
    assert domain_pct == pytest.approx(sum(aspect_pcts) / len(aspect_pcts))
