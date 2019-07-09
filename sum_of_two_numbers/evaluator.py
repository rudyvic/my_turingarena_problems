import random

import turingarena as ta


# for i in range(10):
#     ta.evallib.evaluation.send_data(dict(type="value", key=f"field_{i}", value=i**2))

for _ in range(20):
    value_range = range(-10 ** ta.parameters.digits, 5 * 10 ** ta.parameters.digits)
    a, b = random.choices(value_range, k=2)

    try:
        print(f"Testing {a} + {b} ...", end="")
        with ta.run_algorithm(ta.submission.source) as process:
            c = process.functions.sum(a, b)
            d = process.functions.diff(a, b)
        print(f" answer: {c} {d}", end="\t")
        if c == a + b:
            print(" (correct)", end=" ")
        else:
            print("  (WRONG!)", end=" ")
            ta.goals["correct"] = False
        print(f"(time: {int(process.time_usage * 1000000)} us)")
    except ta.AlgorithmError as e:
        print(f" error: {e}")
        ta.goals["correct"] = False

ta.goals.setdefault("correct", True)



def test_correct_solution():
    with ta.run_algorithm("solutions/correct.cpp") as p:
        assert p.functions.sum(3, 5) == 8
