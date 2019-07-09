from turingarena.evaluation.evaluator import Evaluator
from turingarena.evaluation.util import evaluation_text, evaluation_goals


def evaluate(path):
    return list(Evaluator().evaluate({"source": path}))


def test_evaluation():
    evaluation_events = evaluate("solutions/correct.cpp")
    for line in evaluation_text(evaluation_events).splitlines():
        assert "correct" in line
    goals = evaluation_goals(evaluation_events)
    assert goals["correct"]


def test_evaluation_wrong():
    evaluation_events = evaluate("solutions/always_wrong.py")
    for line in evaluation_text(evaluation_events).splitlines():
        assert "WRONG" in line
    goals = evaluation_goals(evaluation_events)
    assert not goals["correct"]
