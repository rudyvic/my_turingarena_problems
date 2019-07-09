import random

import turingarena as ta
from turingarena.evallib.algorithm import run_algorithm

num_tests = 20
N = 10
        
def get_sum(array):
    done = False
    while(done==False):
        i1 = random.randint(0,N-1)
        i2 = random.randint(0,N-1)
        i3 = random.randint(0,N-1)

        if(i1==i2 or i1==i3 or i2==i3):
            done = False
        else:
            done = True

    return array[i1] + array[i2] + array[i3]



def is_correct(array,indexes,sum):
    a1 = array[indexes[0]]
    a2 = array[indexes[1]]
    a3 = array[indexes[2]]

    if(a1+a2+a3 == sum):
        return True
    else:
        return False



for _ in range(num_tests):
    # create the array in a random way
    array = []
    for _ in range(N):
        array.append(random.randint(0,10 ** 5))

    # take a random sum of 3 distinct elements of the array
    correct = get_sum(array)

    try:
        print(f"Testing {array} with sum {correct} ...", end=" ")
        indexes = [1,2,3]
        with ta.run_algorithm(ta.submission.source) as process:
            answer = process.functions.find_sum(array,N,correct)
            # indexes[0] = process.functions.get_result(0)
            # indexes[1] = process.functions.get_result(1)
            # indexes[2] = process.functions.get_result(2)
        
        if is_correct(array,indexes,correct)==True:
            print('correct, number of guess')
        else:
            print('WRONG!')
            ta.goals["correct"] = False
    #     print(f" answer: {c} {d}", end="\t")
    #     if c == a + b:
    #         print(" (correct)", end=" ")
    #     else:
    #         print("  (WRONG!)", end=" ")
    #         ta.goals["correct"] = False
    #     print(f"(time: {int(process.time_usage * 1000000)} us)")
    except ta.AlgorithmError as e:
        print(f" error: {e}")
        ta.goals["correct"] = False

ta.goals.setdefault("correct", True)
