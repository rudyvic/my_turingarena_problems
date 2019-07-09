import random

import turingarena as ta

def compare(n, a, b):
    for i in range(0,n):
        if a[i] != b[i]:
            return i
    return -1

numElem = 10
numIter = 10

for _ in range(numIter):
    a = random.choices(range(10 ** 4, 10 ** 5), k=numElem)
    b = a.copy()

    print()
    for x in a:
        print(f"{x}", end=" ")
    print()

    for x in b:
        print(f"{x}",end=" ")
    print()

    try:
        with ta.run_algorithm(ta.submission.source) as process:
            index = process.functions.compare_two_arrays(len(a), a, b)
        if index == compare(len(a),a,b):
            print(f"correct! {index}")
        else:
            ta.goals["correct"] = False
            print(f"WRONG! Result is {index} but it was expected {compare(len(a),a,b)}")
    except ta.AlgorithmError as e:
        ta.goals["correct"] = False
        print(e)

ta.goals.setdefault("correct", True)
