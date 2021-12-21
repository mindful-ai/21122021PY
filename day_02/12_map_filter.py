Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> T = [100, 110, 112, 114, 119]
>>> F = []
>>> for t in T:
	F.append(t * 1.8 + 32)

	
>>> F
[212.0, 230.0, 233.6, 237.20000000000002, 246.20000000000002]
>>> def conv(t):
	return t * 1.8 + 32

>>> F1 = map(conv, T)
>>> F1
<map object at 0x0000020256CF3F28>
>>> list(F1)
[212.0, 230.0, 233.6, 237.20000000000002, 246.20000000000002]
>>> f = lambda t : t * 1.8 + 32
>>> type(f)
<class 'function'>
>>> f(100)
212.0
>>> f(101)
213.8
>>> F2 = map(lambda t : t * 1.8 + 32, T)
>>> F2
<map object at 0x0000020256C9BFD0>
>>> list(F2)
[212.0, 230.0, 233.6, 237.20000000000002, 246.20000000000002]
>>> 
>>> 
>>> 
>>> L = list(range(100))
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> 
>>> 
>>> F3 = filter(lambda n : n % 11 == 0, L)
>>> F3
<filter object at 0x0000020256CF3FD0>
>>> list(F3)
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> 
>>> s = ["red", "green", "blue", "yellow", "pink", "purple"]
>>> s1 = filter(lambda s : len(s) >= 5, s)
\
>>> list(s1)
['green', 'yellow', 'purple']
>>> 
>>> 
>>> 
>>> amts = ["15,700", "34,678
	
SyntaxError: EOL while scanning string literal
>>> amts = ["15,700", "34,678", "78,000", "45,345"]
>>> s = "15,700"
>>> s * 0.15
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s * 0.15
TypeError: can't multiply sequence by non-int of type 'float'
>>> int(s) * 0.15
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(s) * 0.15
ValueError: invalid literal for int() with base 10: '15,700'
>>> s.replace(',','')
'15700'
>>> amt15 = map(lambda a : int(a.replace(',','')) * 0.15, amts)
>>> amt15
<map object at 0x0000020256D29A20>
>>> list(amt15)
[2355.0, 5201.7, 11700.0, 6801.75]
>>> 
