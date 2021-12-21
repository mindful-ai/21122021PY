Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ['red', 'green', 'blue']
>>> type(L)
<class 'list'>
>>> T = ('red', 'green', 'blue')
>>> type(T)
<class 'tuple'>
>>> 
>>> 
>>> # ---------------------- list and tuple difference
>>> 
>>> L[1] = 'yellow'
>>> L
['red', 'yellow', 'blue']
>>> T[1]
'green'
>>> T[1] = 'yellow'
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    T[1] = 'yellow'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # tuples are immutable
>>> 
>>> T = ('red', ['green', 'blue'], 'yellow')
>>> T[0] = 'red'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    T[0] = 'red'
TypeError: 'tuple' object does not support item assignment
>>> T[1]= 'red'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    T[1]= 'red'
TypeError: 'tuple' object does not support item assignment
>>> T[2] = 'red'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    T[2] = 'red'
TypeError: 'tuple' object does not support item assignment
>>> T[1]
['green', 'blue']
>>> T[1].append('pink')
>>> T
('red', ['green', 'blue', 'pink'], 'yellow')
>>> 
>>> 
>>> # --------------- adding and removing elements
>>> # NOT PERMITTED
>>> 
>>> # ---------------- rearranging elements
>>> 
>>> reversed(T)
<reversed object at 0x000002262E2689B0>
>>> list(reversed(T))
['yellow', ['green', 'blue', 'pink'], 'red']
>>> sorted(T)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    sorted(T)
TypeError: '<' not supported between instances of 'list' and 'str'
>>> 
>>> T = ('red', 'green', 'blue')
>>> list(reversed(T))
['blue', 'green', 'red']
>>> sorted(T)
['blue', 'green', 'red']
>>> sorted(T, reverse=True)
['red', 'green', 'blue']
>>> 
>>> # T.sort() and T.reverse()
>>> 
>>> # --------------------- iteration
>>> 
>>> for item in T:
	print(item)

	
red
green
blue
>>> 
>>> # ----------------------- numeric tuple
>>> 
>>> # sum(), min(), max(), all() and any() these work
>>> 
>>> # ------------------------ modifying a tuple
>>> 
>>> temp = list(T)
>>> temp
['red', 'green', 'blue']
>>> temp[1] = 'yellow'
>>> temp
['red', 'yellow', 'blue']
>>> T = tuple(temp)
>>> T
('red', 'yellow', 'blue')
>>> 
>>> # ----------------------- unpacking list/tuples
>>> 
>>> T
('red', 'yellow', 'blue')
>>> r, g, b = T
>>> r
'red'
>>> g
'yellow'
>>> b
'blue'
>>> r, g = T
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    r, g = T
ValueError: too many values to unpack (expected 2)
>>> 
>>> T = ('red', 'green', 'yellow', 'blue', 'pink')
>>> a, b, *x = T
>>> a
'red'
>>> b
'green'
>>> x
['yellow', 'blue', 'pink']
>>> x[0]
'yellow'
>>> x[1]
'blue'
>>> x[-1]
'pink'
>>> 
