import random

from turingarena import *
from turingarena.evallib.algorithm import run_algorithm

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
    if((indexes[0]==indexes[1] or indexes[1]==indexes[2]) or indexes[0]==indexes[2]):
        return False

    a1 = array[indexes[0]-1]
    a2 = array[indexes[1]-1]
    a3 = array[indexes[2]-1]

    if(a1+a2+a3 == sum):
        return True
    else:
        return False


num_tests = 20
N = 10
        
all_passed = True
for _ in range(num_tests):
    # create the array in a random way
    array = []
    for _ in range(N):
        array.append(random.randint(0,10 ** 2))

    # take a random sum of 3 distinct elements of the array
    correct = get_sum(array)

    print(f"Testing {array} with sum {correct} ...", end=" ")

    try:
        with run_algorithm(submission.source) as process:
            process.procedures.find_sum(N, array, correct)
            indexes = [process.functions.get_result(i) for i in range(0,3)]
        
            if is_correct(array,indexes,correct)==True:
                print(f"(correct) \t indexes: {indexes}")
            else:
                print("WRONG!")
                all_passed = False
                goals["correct"] = False
        print(f"(time: {int(process.time_usage * 1000000)} us)",end="\n\n")
    except AlgorithmError as e:
        print(f" error: {e}")
        goals["correct"] = False
if(all_passed==True):
    print("All test passed correctly.")
else:
    print("NOT all test passed correctly...")

goals.setdefault("correct", True)
