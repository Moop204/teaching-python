# Numbers

For this exercise we will familiarise you with how numbers are used in Python and the way they are represented.

While there are more ways to represent numbers we will focus on the two basic ways: 

* Integers
* Decimals

Usually for other languages each way to represent a number needs a different type to represent it. Luckily in Python it is all one type, the `number` type. This means you can have integers and decimals be applied together. 

With other languages you may hear about 'signed' and 'unsigned' numbers. Signed numbers are those that can differentiate between positive and negative while unsigned numbers can only be positive. Again, in Python all numbers are signed since the hard work is done for you by Python.

## Basic Operators
Just like you would expect a computer can do all the normal operations that you learned in highschool. Wherever you see a number remember that you can replace that number with a variable that represents a number as well.


| Operation     | Operator  | Example  | Example Result |
|---------------|-----------|----------|----------------|
| Addition      |  +        | 4 + 12.5 | 16.5           |
| Subtraction   |  -        | 12 - 100 | -88            |
| Multiplication|  *        | 12 * 4   | 48             |
| Division      |  /        | 13 / 5   | 2.6            |
| Exponential   |  **       | 2**3     | 8              |

## Additional Operators

Additional operations are available in python.

| Operation       | Operator  | Example  | Example Result |
|-----------------|-----------|----------|----------------|
| Modulo          |  %        | 13//5    | 3              |
| Integer Division|  //       | 13//5    | 2              |

Modulo - This obtains the remainder of the first number when divided by the second number.

Integer Dvision - This counts how many times the first number can be divided by the second. 

## Assignment Operators
There will be many occasions where you will be applying an operation to a variable that involves itself. This can be done for example when you are counting something and need to add 1 to the count. Instead of fully writing these variables we can use assignment operators as shorthand to apply the operation to the same variable that it is used for. 

Example:
```
a = a + 3 
```
can be shortened to
```
a += 3
```

| Operation     | Operator   | Example  | 
|---------------|------------|----------|
| Addition      |  +=        | t += 7         |
| Subtraction   |  -=        | countdown -= 1 |
| Multiplication|  *=        | length*=2      |
| Division      |  /=        | divide_by_3/=3 |

## Assigning a Number
You can assign a `number` literal to a variable

```python
a = 10

where 10    is number literal
      a     is variable
```

You can assign another variable that is a number to another variable

```python
a = 4
b = a
```

Thats all you need to know about numbers!