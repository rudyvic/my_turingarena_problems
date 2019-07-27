import random

from turingarena import *
from turingarena.evallib.algorithm import run_algorithm

def print_vett(vett, n):
    for i in range(n):
        print(f"{vett[i]}",end=" ")
    print("\n")

def check(vett, res, n):
    vett = sorted(vett)
    d = 0
    all_passed = True

    for i in range(n-1):
        if vett[i] != vett[i+1]:
            d = d + 1

    if d != 0:
        d = d + 1

    if res == d:
        if(n <= 100):
            print(f"small input correct! [res: {d}]")
            goals["small_input_correct"] = True
        elif(n <= 1000):
            print(f"medium input correct! [res: {d}]")
            goals["medium_input_correct"] = True
        else:
            print(f"large input correct! [res: {d}]")
            goals["large_input_correct"] = True
    else:
        print("WRONG!")
        if(n <= 100):
            print(f"small input correct answer is [{d}] instead of [{res}]")
            goals["small_input_correct"] = False
            all_passed = False
        elif(n <= 1000):
            print(f"medium input correct answer is [{d}] instead of [{res}]")
            goals["medium_input_correct"] = False
            all_passed = False
        else:
            print(f"large input correct answer is [{d}] instead of [{res}]")
            goals["large_input_correct"] = False
            all_passed = False

    return all_passed


for i in range(3):
    all_passed_global = True
    print(f"\nSUBTASK {i + 1}")
    for _ in range(10):
        n = 10 ** (i+2)
        a = random.choices(range(1, 10 ** 4), k=n)
        try:
            with run_algorithm(submission.source) as process:
                process.procedures.sort(n, a)
                c = process.functions.distinct(n)

        except AlgorithmError as e:
            print(e)
            break
            # all_passed = False

        all_passed = check(a, c, n)
        if(all_passed == False):
            all_passed_global = False

    #print_vett(a,n)

    if(all_passed_global == False):
        print(f"\n[WARNING] Not all subtask's {i+1} test passed!\n")

    else:
        print(f"\n[ACCEPTED] All subtask's {i+1} test passed!\n")


