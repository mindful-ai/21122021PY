Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Strings
>>> 
>>> s = "computer" # s = 'computer'
>>> type(s)
<class 'str'>
>>> 
>>> # ------------------------------- subscripting
>>> 
>>> s[0]
'c'
>>> s[1]
'o'
>>> s[2]
'm'
>>> s[-1]
'r'
>>> s[-2]
'e'
>>> s[-3]
't'
>>> s[3:5]
'pu'
>>> # [5:10] => 5, 6, 7, 8, 9
>>> # [m:n] => m, m+1, m+2 ... n-1
>>> s[3:6]
'put'
>>> s[0:3]
'com'
>>> s[:3]
'com'
>>> s[5:8]
'ter'
>>> s[5:]
'ter'
>>> s[:]
'computer'
>>> s[0:8]
'computer'
>>> s[1:6]
'omput'
>>> s[1:6:2]
'opt'
>>> s[1:6:3]
'ou'
>>> s[::2]
'cmue'
>>> s[::-1]
'retupmoc'
>>> # -------------------------------- Operators
>>> 
>>> 'abc' + 'def'
'abcdef'
>>> 
>>> 'ac' * 6
'acacacacacac'
>>> 
>>> len(s)
8
>>> s
'computer'
>>> 
>>> type(s) == str
True
>>> type(s) == int
False
>>> isinstance(s, str)
True
>>> isinstance(s, int)
False
>>> 
>>> s
'computer'
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> # ------------------------------ String operations
>>> 
>>> s = "computer"
>>> 
>>> 
>>> # --------- Case based functions
>>> 
>>> s.upper()
'COMPUTER'
>>> 
>>> s
'computer'
>>> s[0]
'c'
>>> s[0] = "P"
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s[0] = "P"
TypeError: 'str' object does not support item assignment
>>> 
>>> s = "python'
SyntaxError: EOL while scanning string literal
>>> s = "python"
>>> s[0] = J # Jython
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s[0] = J # Jython
NameError: name 'J' is not defined
>>> s[1:]
'ython'
>>> 'J' + s[1:]
'Jython'
>>> s = 'J' + s[1:]
>>> s
'Jython'
>>> s[0] = 'P'
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s[0] = 'P'
TypeError: 'str' object does not support item assignment
>>> # ------------- concept of immutability: doesn't allow inplace changes -------#
>>> 
>>> s
'Jython'
>>> s = computer
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    s = computer
NameError: name 'computer' is not defined
>>> s = 'computer;
SyntaxError: EOL while scanning string literal
>>> s = 'computer'
>>> s
'computer'
>>> s.upper()
'COMPUTER'
>>> s
'computer'
>>> s1 = s.upper()
>>> s
'computer'
>>> s1
'COMPUTER'
>>> s = s.upper() # overwriting the contents of s
>>> s
'COMPUTER'
>>> s.lower()
'computer'
>>> s.capitalize()
'Computer'
>>> s
'COMPUTER'
>>> 
>>> 
>>> # --------------------------- questioning/checking
>>> 
>>> '123'.isdigit()
True
>>> '12.45A'.isdigit()
False
>>> 'ASD'.isalpha()
True
>>> 'ASD234'.isalpha()
False
>>> 'ASD324'.isalnum()
True
>>> s.isupper()
True
>>> s.islower()
False
>>> ' '.isspace()
True
>>> 'AD'.isspace()
False
>>> 
>>> # ---------------------------- searching
>>> 
>>> s
'COMPUTER'
>>> s.find('PUT')
3
>>> s1 = "mississippi"
>>> s1.find('i')
1
>>> s1.rfind('i')
10
>>> s1.count('i')
4
>>> s1.count('ss')
2
>>> 
>>> # --------------------------- modifications
>>> 
>>> salary = "15,56,888"
>>> int(salary)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    int(salary)
ValueError: invalid literal for int() with base 10: '15,56,888'
>>> salary.replace(',','')
'1556888'
>>> salary
'15,56,888'
>>> salary = salary.replace(',','')
>>> salary
'1556888'
>>> int(salary)
1556888
>>> hike = int(salary) * 0.15
>>> hike
233533.19999999998
>>> newsalary = int(salary) + hike
>>> newsalary
1790421.2
>>> 
>>> 
>>> ip = "123-45-1-1"
>>> newip = ip.replace('-', '.')
>>> newip
'123.45.1.1'
>>> 
>>> 
>>> # Justification
>>> 
>>> s
'COMPUTER'
>>> s.ljust(30)
'COMPUTER                      '
>>> s.rjust(30, '+')
'++++++++++++++++++++++COMPUTER'
>>> 
>>> 
>>> # Stripping
>>> 
>>> s = "    23456     "
>>> s.strip()
'23456'
>>> s.lstrip()
'23456     '
>>> s.rstrip()
'    23456'
>>> 
>>> 
>>> # startswith and endswith
>>> 
>>> url = "www.google.com"
>>> url.startswith("http")
False
>>> url.endswith("com")
True
>>> 
>>> # Split and join
>>> 
>>> text = "mary had a little lamb"
>>> text.split()
['mary', 'had', 'a', 'little', 'lamb']
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> L = ['mary', 'had', 'a', 'little', 'lamb']
>>> type(L)
<class 'list'>
>>> '-'.join(L)
'mary-had-a-little-lamb'
>>> 
