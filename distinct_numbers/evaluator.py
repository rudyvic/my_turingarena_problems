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

    for i in range(n-1):
        if vett[i] != vett[i+1]:
            d = d + 1

    if d != 0:
        d = d + 1

    if res == d:
        print(f"correct! [{d}]")
    else:
        print("WRONG!")
        all_passed = False

all_passed = True
for _ in range(10):
    n = 10
    a = random.choices(range(10 ** 1, 10 ** 2), k=n)

    try:
        with run_algorithm(submission.source) as process:
            process.procedures.sort(n, a)
            c = process.functions.distinct(n)

    except AlgorithmError as e:
        print(e)
        all_passed = False


    check(a, c, n)

    print_vett(a,n)

