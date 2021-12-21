Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Helo ORacle')
Helo ORacle
>>> a = 4 + 5
>>> a
9
>>> 
====== RESTART: C:/Users/Purushotham/Desktop/oralcepy/day_01/01_test.py ======
Hello Oracle
66
>>> # ---------------------------- Numbers
>>> 
>>> a = 5
>>> b = 2
>>> type(a)
<class 'int'>
>>> f = 5.6
>>> type(f)
<class 'float'>
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 
>>> print(a)
5
>>> print(b)
2
>>> a
5
>>> b
2
>>> f
5.6
>>> a + 0
5
>>> a
5
>>> # ---------------------------- Operators
>>> 
>>> # -------------- Arithmetic Operators
>>> 
>>> a + b
7
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> a % b
1
>>> a // b
2
>>> a ** b
25
>>> 
>>> # ----------------- Relational Operators
>>> 
>>> a > b # Is a greater than b?
True
>>> a < b
False
>>> a >= b
True
>>> a <= b
False
>>> a == b
False
>>> a != b
True
>>> a == b * 2 + 1
True
>>> 
>>> (a == b) ? "Python" : "Perl"
SyntaxError: invalid syntax
>>> if (a == b):
	print("python")
else:
	print("perl")

	
perl
>>> 
>>> # ----------------- Logical Operators
>>> 
>>> a
5
>>> b
2
>>> a > b and a > 10
False
>>> a > b and a != 0
True
>>> a > b or a > 10
True
>>> a > b and not a > 10
True
>>> 
>>> # ------------------------------- built in function for numbers
>>> 
>>> a - b
3
>>> b - a
-3
>>> abs(a - b)
3
>>> abs(b - a)
3
>>> a = 100
>>> oct(a)
'0o144'
>>> hex(a)
'0x64'
>>> bin(a)
'0b1100100'
>>> s = '56'
>>> s + 10
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s + 10
TypeError: can only concatenate str (not "int") to str
>>> int(s) + 10
66
>>> a = '1001010'
>>> int(a) + 10
1001020
>>> int(a, 2) + 10
84
>>> it(a, 2)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    it(a, 2)
NameError: name 'it' is not defined
>>> int(a, 2)
74
>>> s = '123.45'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '123.45'
>>> float(s)
123.45
>>> chr(56)
'8'
>>> chr(87)
'W'
>>> ord('8')
56
>>> ord('W')
87
>>> pow(7, 2)
49
>>> # ------------------------ built in modules
>>> 
>>> a = 99
>>> b = 33
>>> # gcd ??
>>> 
>>> gcd(a, b)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    gcd(a, b)
NameError: name 'gcd' is not defined
>>> import math
>>> gcd(a, b)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    gcd(a, b)
NameError: name 'gcd' is not defined
>>> math.gcd(a, b)
33
>>> a = 90
>>> sin(90)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    sin(90)
NameError: name 'sin' is not defined
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(90 * 3.14159/180)
0.9999999999991198
>>> math.sin(90 * math.pi/180)
1.0
>>> math.sin(math.radians(90))
1.0
>>> # How to take inputs from the users?
>>> 
>>> print("The value is", a)
The value is 90
>>> print("The values are %d and %d" % (a, b))
The values are 90 and 33
>>> 
>>> 
>>> input()
45
'45'
>>> a = input()
45
>>> a
'45'
>>> a = input("Enter a number: ")
Enter a number: 45
>>> a
'45'
>>> a + 56
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a + 56
TypeError: can only concatenate str (not "int") to str
>>> int(a) + 56
101
>>> a = int(input("Enter a number: "))
Enter a number: 45
>>> a
45
>>> a + 56
101
>>> 
