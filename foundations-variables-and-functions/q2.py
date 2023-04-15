import contextlib, io

"""
Even function

Make a function that checks if the incoming number is even

Example Test:
5
> False

4
> True
"""
def is_even(num)->bool:
    # Write your code underneath
    return True

"""
Even function

Make a function that checks if the incoming number is odd

Example Test:
5
> True

4
> False
"""
def is_odd(num)->bool:
    # Write your code underneath
    return True

"""
Is Divisible function

Make a function that determines if the numerator is divisible by the divisor

Example Tests:
4 5
False

16 8
True
"""
def is_divisible(numerator, divisor)->bool:
    # Write your code underneath
    return True

"""
Identifying shape function

You are given the length of four sides of a shape. Print
out what shape is made by the length of edges found in 
the arguments. 

When there are only three sides (meaning one side is None)
then the shape should be triangle and it should print
"I am a triangle!"

However if only three sides are given and they are all the 
same print out
"I am an equilateral triangle!"

When all four sides are the same then it should print
"I am a square!"

When two pairs of sides are equal then it should print
"I am a rectangle!"

When there are four sides then it should print
"I am a quadrilateral!"

If there are not enough sides to make any shape then
print
"I am no shape D:"

Limits:
If there is a side then it has a value of 1 or higher
If there is no side then it has a value of None
"""
def what_is_shape(side_a, side_b, side_c, side_d)->None:
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        # Write your code underneath
        print("idk")
        # Write your code above
    return f.getvalue()