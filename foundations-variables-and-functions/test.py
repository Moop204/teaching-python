from q1 import double, average 
import random
import sys

def output_result(comparator, input, header=""):
    print(header)

    error_logs = []
    for i, (expect, test) in enumerate(comparator):
        if(expect == test):
            print(f"Test {i+1}: Success")
        else:
            failed_notif = f"Test {i+1}: Failed"
            print(failed_notif)
            error_logs.append(failed_notif)

            failed_detail = f"Input: {input[i]} Expected: {expect} Received: {test}"
            print(failed_detail)
            error_logs.append(failed_detail)
    print("Errors")
    for log in error_logs:
        print(log)
    

def chunk(list, size_of_chunk):
    for i in range(0, len(list), size_of_chunk):
        yield list[i: i+size_of_chunk]


def test_double():
    input_numbers = [
        *[random.randint(-1000, 1000) for i in range(15)], 
        *[random.randint(-1000, 1000)*random.random() for i in range(15)]]
    

    expected_numbers = [2*num for num in input_numbers]
    test_numbers = [double(num) for num in input_numbers]
    comparator = zip(expected_numbers, test_numbers)
    output_result(comparator, input_numbers, "Q1")

def test_average():
    base_numbers = [
        *[random.randint(-1000, 1000) for i in range(15)], 
        *[random.randint(-1000, 1000)*random.random() for i in range(15)]]
    input_numbers = list(chunk(base_numbers, 3))
    expected_numbers = [sum(num)/len(num) for num in input_numbers]
    test_numbers = [average(*num) for num in input_numbers]
    comparator = zip(expected_numbers, test_numbers)
    output_result(comparator, input_numbers, "Q2")



def all_tests():
    if len(sys.argv) < 2:
        print("Available tests")
        for i in range(1,2):
            print(f"q{i}")
    elif sys.argv[1] == "q1":
        test_double()
        test_average()
    else:
        print("Invalid test number")
all_tests()