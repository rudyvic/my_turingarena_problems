import random

from turingarena import *
from turingarena.evallib.algorithm import run_algorithm

def get_sum(array,N):
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

def do_test(num_tests,N,num_subtask,max_exp):
    all_passed = True
    print(f"SUBTASK #{num_subtask}")

    for num_test in range(num_tests):
        # create the array in a random way
        array = []
        for _ in range(N):
            array.append(random.randint(0,10 ** max_exp))

        # take a random sum of 3 distinct elements of the array
        correct = get_sum(array,N)

        # print(f"[CASE {num_subtask}] Testing {array} with sum {correct} ...", end=" ")
        print(f"Test {num_test+1}/{num_tests}: {N} elements, values between 0 and {10**max_exp} -->", end=" ")

        try:
            with run_algorithm(submission.source) as process:
                process.procedures.find_sum(N, correct, array)
                indexes = [process.functions.get_result(i) for i in range(0,3)]
            
                if is_correct(array,indexes,correct)==True:
                    # print(f"(correct) \t indexes: {indexes}")
                    print("CORRECT")
                else:
                    print("WRONG!")
                    all_passed = False
                    # goals["correct"] = False
            print(f"(time: {int(process.time_usage * 1000000)} us)",end="\n")
        except AlgorithmError as e:
            print(f" error: {e}")
            all_passed = False
            # goals["correct"] = False
    if(all_passed==True):
        print(f"[SUBTASK {num_subtask}] All tests passed correctly.",end="\n\n\n")
    else:
        print(f"[SUBTASK {num_subtask}] NOT all tests passed correctly...",end="\n\n\n")

    # goals.setdefault("correct", True)
    return all_passed


############ MAIN ##############

goals["small_input"] = do_test(10,10,1,2)
goals["medium_input"] = do_test(20,1000,2,5)
goals["large_input"] = do_test(5,10000,3,3)

print("\nSummary")
print(f"{goals}")
