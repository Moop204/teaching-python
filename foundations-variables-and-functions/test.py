from q1 import double, average 
from q2 import is_even, is_odd, is_divisible, what_is_shape

import random
import sys
import contextlib, io

def output_result(comparator, input, header=""):
    print(header)

    for i, (expect, test) in enumerate(comparator):
        if(expect == test):
            print(f"Test {i+1}: Success")
        else:
            failed_notif = f"Test {i+1}: Failed"
            print(failed_notif)

            failed_detail = f"Input: {input[i]} \nExpected: {expect} \nReceived: {test}\n"
            print(failed_detail)
            break
    

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
    output_result(comparator, input_numbers, "Double Question")

def test_average():
    base_numbers = [
        *[random.randint(-1000, 1000) for i in range(15)], 
        *[random.randint(-1000, 1000)*random.random() for i in range(15)]]
    input_numbers = list(chunk(base_numbers, 3))
    expected_numbers = [sum(num)/len(num) for num in input_numbers]
    test_numbers = [average(*num) for num in input_numbers]
    comparator = zip(expected_numbers, test_numbers)
    output_result(comparator, input_numbers, "Average Question")

def test_is_even():
    input_numbers = [2, 4, 1, 3,
        *[random.randint(-1000, 1000) for i in range(15)], 0]
    expected_numbers = [True if num % 2 == 0 else False for num in input_numbers]
    test_numbers = [is_even(num) for num in input_numbers]
    comparator = zip(expected_numbers, test_numbers)
    output_result(comparator, input_numbers, "Even Question")

def test_is_odd():
    input_numbers = [2, 4, 1, 3,
        *[random.randint(-1000, 1000) for i in range(15)], 0]
    expected_numbers = [True if num % 2 == 1 else False for num in input_numbers]
    test_numbers = [is_odd(num) for num in input_numbers]
    comparator = zip(expected_numbers, test_numbers)
    output_result(comparator, input_numbers, "Odd Question")

def test_is_divisible():
    input_numbers = [4, 2, 3, 1, 7, 40,
        *[random.randint(-1000, 1000) for i in range(8)], 
        77, 11, 100, 0, 0, 100,
        *[random.randint(-1000, 1000) for i in range(8)], 
        -16, 4, 26, -13        
        ]
    expected_numbers = [True if num % 2 == 1 else False for num in input_numbers]
    test_numbers = [is_divisible(num) for num in input_numbers]
    comparator = zip(expected_numbers, test_numbers)
    output_result(comparator, input_numbers, "Divisible Question")

def test_is_divisible():
    input_numbers = [4, 2, 3, 1, 7, 40,
        *[random.randint(-1000, 1000) for i in range(8)], 
        77, 11, 100, 0, 0, 100,
        *[random.randint(-1000, 1000) for i in range(8)], 
        -16, 4, 26, -13        
        ]
    expected_numbers = [True if num % 2 == 1 else False for num in input_numbers]
    test_numbers = [is_odd(num) for num in input_numbers]
    comparator = zip(expected_numbers, test_numbers)
    output_result(comparator, input_numbers, "Divisible Question")

def test_what_is_shape():
    base_numbers = [
        5, None, 3, 4,
        None, 2, 3, 4,
        5, 6, 7, None,
        5, 6, None, 4,
        5, None, 3, None,
        None, None, None, None,
        1, 1, 1, 1,
        1, 2, 3, 4,
        22, 14, 14, 22,
        76, 1465, 76, 1465,
        1, 1, 99, 99,
        *[random.randint(1, 1000) for i in range(16)], 
        *[random.randint(1, 1000)*random.random() for i in range(16)]]
    input_numbers = list(chunk(base_numbers, 4))
    expected_numbers = []
    for nums in input_numbers:
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            none_count = 0
            map_lengths = {}
            for num in [*nums]:
                if num == None:
                    none_count+=1
                if num in map_lengths:
                    map_lengths[num]+=1
                else:
                    map_lengths[num] = 1        
            if none_count > 1:
                print("I am no shape D:")
            elif none_count == 1 and any(map_lengths[key]==3 for key in map_lengths.keys()):
                print("I am an equilateral triangle!")
            elif none_count == 1:
                print("I am a triangle!")
            elif len(map_lengths.keys()) == 1:
                print("I am a square!")
                print("I am a rectangle!")
                print("I am a quadrilateral!")
            elif len(map_lengths.keys()) == 2:
                print("I am a rectangle!")
                print("I am a quadrilateral!")
            else:
                print("I am a quadrilateral!")
        expected_numbers.append(f.getvalue())

    test_numbers = [what_is_shape(*num) for num in input_numbers]
    comparator = zip(expected_numbers, test_numbers)
    output_result(comparator, input_numbers, "Shape Question")
    
def all_tests():
    if len(sys.argv) < 2:
        print("Available tests")
        for i in range(1,3):
            print(f"q{i}")
    else:
        question_selection = sys.argv[1]
        if question_selection == "q1":
            test_double()
            test_average()
        elif question_selection == "q2":
            test_is_even()
            test_is_odd()
            test_is_divisible()
            test_what_is_shape()
        else:
            print("Invalid test number")
all_tests()