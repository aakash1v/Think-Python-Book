"""

1. In a print statement, what happens if you leave out one of the parentheses, or
both?
print (5        -->SyntaxError: '(' was never closed

2. If you are trying to print a string, what happens if you leave out one of the quota‐
tion marks, or both?
print(okay)     --> NameError: name 'okay' is not defined

3. You can use a minus sign to make a negative number like -2. What happens if
you put a plus sign before a number? What about 2++2?
print(+5)       --> Everything is fine
print(2++2)     --> NO problem 

4. In math notation, leading zeros are okay, as in 02. What happens if you try this in
Python?
print(02)       -->SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers 

5. What happens if you have two values with no operator between them?
print(50 100)   -->SyntaxError: invalid syntax. Perhaps you forgot a comma?
"""
