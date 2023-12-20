"""
Exercise 2-1.
Repeating my advice from the previous chapter, whenever you learn a new feature,
you should try it out in interactive mode and make errors on purpose to see what
goes wrong.
• We’ve seen that n = 42 is legal. What about 42 = n?
>>> 42=n -->SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
    ^^
• How about x = y = 1?
>>> x =y =1  -->Everything is fine...
• In some languages every statement ends with a semicolon, ;. What happens if
you put a semicolon at the end of a Python statement?
>>> print("hello");         --> no problem with semicolon
hello

18 | Chapter 2: Variables, Expressions and Statements
• What if you put a period at the end of a statement?
--Done
• In math notation you can multiply x and y like this: xy. What happens if you try
that in Python?
>>> x =4
>>> y =5
>>> xy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'xy' is not defined. Did you mean: 'x'?
"""