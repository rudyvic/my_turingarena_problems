import random

from turingarena import *
from turingarena.evallib.algorithm import run_algorithm

def reverse(a, n):
    b = []
    for i in range(0,n):
        b.append(a[n-i-1])
    return b

all_passed = True
for _ in range(10):
    n = 3
    a = random.choices(range(10 ** 4, 10 ** 5), k=n)

    try:
        with run_algorithm(submission.source) as process:
            process.procedures.reverse_array(n, a)
            b = [process.functions.get_element(i) for i in range(n)]
    except AlgorithmError as e:
        print(e)
        all_passed = False
    if b == reverse(a,n):
        print(f"correct! {a} {b}")
    else:
        print(f"WRONG! {a} {b}")
        all_passed = False
