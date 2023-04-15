# Controls and Conditions
We can use controls in the code we write to direct the program down certain paths depending on the situation. 

## Truth
When we consider the truth-fulness of a statement in code it is either true or false. We call these `boolean` values.

We have a few relational operators including:

| Operation            | Operator   | Example  | 
|----------------------|------------|----------|
| Equal                |  ==        | a == b   |
| Not Equal            |  !=        | a != b   |
| Less Than            |  <         | a < b    |
| Larger Than          |  >         | a > b    |
| Less Than or Equal   |  <=        | a <= b   |
| Larger Than or Equal |  >=        | a >= b   |

## Controls
Now that we can define something as truthful or not we can use that to guide the logic of a program. Control statements use these truth values to figure out what to do.

### IF Statements
If statements let you go down a path under the if statement **if** the condition is met. We have other keywords that can also be used with `if`. 


```python
if a > b:
    print("a is larger than b")
elif b > a:
    print("b is larger than a")
else:
    print("a is the same as b")
```

When we use `elif` we mean "else if". That can only be used after another `if` or `elif` statement and means that they only check this conditon if the previous ones did not pass.

Lets take a look at this example

```python
def test_1(a, b, c):
    if a > c:
        print("a is larger than c")
    elif b > c:
        print("b is larger than c")

def test_2(a, b):
    if a > c:
        print("a is larger than c")
    if b > c:
        print("b is larger than c")

# For a = 10, b = 20, c = 5
# test_1 prints "a is larger than b"
# test_2 prints "a is larger than b" and "b is larger than c" 
# because test_2 does not use an elif
```

We put `else` at the end of either `if` or `elif` to accept every condition that reaches it without 
reaching any of the conditions before it. 

```python
if a == 0:
    print("a is exactly 0")
else:
    print("a is something but it isn't 0")
```

## AND and OR
Usually the conditions need to be complex and involve multiple variables. We can connect the 
truthfulness of these variables using AND and OR logical operators. 

| Operation            | Operator              | Example    | 
|----------------------|-----------------------|------------|
| AND                  |  and (python), && (c) | a and b    |
| OR                   |  or (python), || (c)  | a or b     |
| NOT                  |  not (python), ! (c)  | not a or b |  

AND operators require both operands to be TRUE for the statement to be true. Unlike maths,
there is a slight difference in the order of the operands. The leftmost one is evaluated
first so if that fails the program won't check the other. This is called short-circuiting evaluation.

| a            | b      | Result  | 
|--------------|--------|---------|
| True         |  True  | True    |
| False        |  True  | False   |
| False        |  False | False   |

OR operators require at least ONE of the operands to be TRUE for the statement to be true. 
Short-circuit evaluation for OR operators also exists so the leftmost one is evaluated
first and if that succeeds it won't check the other.

| a            | b      | Result  | 
|--------------|--------|---------|
| True         |  True  | True    |
| False        |  True  | True    |
| False        |  False | False   |

