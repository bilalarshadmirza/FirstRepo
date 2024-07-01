Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3+5
8
>>> a = "hello"
>>> b = 5
>>> c = a + b
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c = a + b
TypeError: can only concatenate str (not "int") to str
>>> c = a + "b"
>>> b = "world"
>>> c = a + b
>>> c
'helloworld'
>>> b = 5
... c = a + b
SyntaxError: multiple statements found while compiling a single statement
>>> b = 5
... c = a + b
SyntaxError: multiple statements found while compiling a single statement
>>> c
'helloworld'
