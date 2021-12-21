Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LISTS
>>> L = ['red', 'green', 'blue', 23, 45, 67, 1.45, -4, [1, 2, 3]]
>>> type(L)
<class 'list'>
>>> 
>>> # -------------------------- accessing elements
>>> L[0]
'red'
>>> L[:3]
['red', 'green', 'blue']
>>> L[-1]
[1, 2, 3]
>>> L[-1][1]
2
>>> L[::-1]
[[1, 2, 3], -4, 1.45, 67, 45, 23, 'blue', 'green', 'red']
>>> L[::2]
['red', 'blue', 45, 1.45, [1, 2, 3]]
>>> L[1::2]
['green', 23, 67, -4]
>>> 
>>> # ---------------------------- mutable nature of lists
>>> 
>>> L[1]
'green'
>>> L[1] ='lightgreen'
>>> L
['red', 'lightgreen', 'blue', 23, 45, 67, 1.45, -4, [1, 2, 3]]
>>> 
>>> L[2]
'blue'
>>> L[2][1]
'l'
>>> L[2][1] = 'x'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    L[2][1] = 'x'
TypeError: 'str' object does not support item assignment


>>> L[-1]
[1, 2, 3]
>>> L[-1][2]
3
>>> L[-1][2] = 5
>>> L
['red', 'lightgreen', 'blue', 23, 45, 67, 1.45, -4, [1, 2, 5]]
>>> 
>>> # ---------------------------------- operators
>>> 
>>> L1 = [1, 2, 3]
>>> L2 = [4, 5, 6]
>>> L1 + L2
[1, 2, 3, 4, 5, 6]
>>> 
>>> L1 * 2
[1, 2, 3, 1, 2, 3]
>>> 
>>> len(L1 + L2)
6
>>> type(L1) == list
True
>>> del L1
>>> del L2
>>> 
>>> # ------------------------------------ add elements
>>> 
>>> L = ['red', 'green', 'blue']
>>> L.append('brown')
>>> L
['red', 'green', 'blue', 'brown']
>>> L.append('yellow')
>>> L
['red', 'green', 'blue', 'brown', 'yellow']
>>> L.insert(1, 'orange')
>>> L
['red', 'orange', 'green', 'blue', 'brown', 'yellow']
>>> 
>>> L1 = ['white', 'grey' , 'black']
>>> L.extend(L1)
>>> L
['red', 'orange', 'green', 'blue', 'brown', 'yellow', 'white', 'grey', 'black']
>>> ['red', 'orange', 'green', 'blue', 'brown', 'yellow', 'white', 'grey', 'black']
['red', 'orange', 'green', 'blue', 'brown', 'yellow', 'white', 'grey', 'black']
>>> 
>>> 
>>> L2 = ['cyan', 'pink']
>>> L = ['red', 'green', 'blue']
>>> L[1]
'green'
>>> L[1] = L2
>>> L
['red', ['cyan', 'pink'], 'blue']
>>> L[1]
['cyan', 'pink']
>>> 
>>> L = ['red', 'green', 'blue']
>>> L[1:2]
['green']
>>> L[1:2] = L2
>>> L
['red', 'cyan', 'pink', 'blue']
>>> 
>>> 
>>> # ------------------------------------ removing elements
>>> 
>>> L
['red', 'cyan', 'pink', 'blue']
>>> L.pop()
'blue'
>>> L
['red', 'cyan', 'pink']
>>> L.pop(1)
'cyan'
>>> L
['red', 'pink']
>>> 
>>> 'pink' in L
True
>>> 'apples' in L
False
>>> L.remove('pink')
>>> L
['red']
>>> 
>>> # ---------------------------------- searching elements
>>> 
>>> L = ['red', 'orange', 'green', 'blue', 'brown', 'yellow', 'white', 'grey', 'black']
>>> L.append('red')
>>> L.append('red')
>>> L
['red', 'orange', 'green', 'blue', 'brown', 'yellow', 'white', 'grey', 'black', 'red', 'red']
>>> 
>>> L.index('red')
0
>>> L[1:].index('red')
8
>>> L[1:].index('red') + len(L[:1])
9
>>> L[9]
'red'
>>> 
>>> 
>>> 'white' in L
True
>>> 
>>> 
>>> L.index('white')
6
>>> if 'white' in L:
	print("The index of white is: ", L.index('white')
	      )

	
The index of white is:  6
>>> 
>>> L.count('white')
1
>>> L.count('red')
3
>>> # ---------------------------------- re-arrange elements
>>> 
>>> L
['red', 'orange', 'green', 'blue', 'brown', 'yellow', 'white', 'grey', 'black', 'red', 'red']
>>> 
>>> L = ['red', 'orange', 'green', 'blue', 'brown', 'yellow', 'white', 'grey', 'black']
>>> 
>>> L[::-1]
['black', 'grey', 'white', 'yellow', 'brown', 'blue', 'green', 'orange', 'red']
>>> reversed(L)
<list_reverseiterator object at 0x00000296EAB0BF98>
>>> list(reversed(L))
['black', 'grey', 'white', 'yellow', 'brown', 'blue', 'green', 'orange', 'red']
>>> L
['red', 'orange', 'green', 'blue', 'brown', 'yellow', 'white', 'grey', 'black']
>>> sorted(L)
['black', 'blue', 'brown', 'green', 'grey', 'orange', 'red', 'white', 'yellow']
>>> L
['red', 'orange', 'green', 'blue', 'brown', 'yellow', 'white', 'grey', 'black']
>>> 
>>> 
>>> L.reverse()
>>> L
['black', 'grey', 'white', 'yellow', 'brown', 'blue', 'green', 'orange', 'red']
>>> L.sort()
>>> L
['black', 'blue', 'brown', 'green', 'grey', 'orange', 'red', 'white', 'yellow']
>>> L.sort(reverse=True)
>>> L
['yellow', 'white', 'red', 'orange', 'grey', 'green', 'brown', 'blue', 'black']
>>> 
>>> # -------------------------------- iteration
>>> 
>>> for item in L:
	print(item)

	
yellow
white
red
orange
grey
green
brown
blue
black
>>> 
>>> for item in L:
	print(item.upper(), end=' ')

	
YELLOW WHITE RED ORANGE GREY GREEN BROWN BLUE BLACK 
>>> 
>>> # ------------------------------------ numeric lists
>>> 
>>> L = [0, 1, 2, 3 , 4, 5]
>>> min(L)
0
>>> max(L)
5
>>> any(L)
True
>>> all(L)
False
>>> all([1:])
SyntaxError: invalid syntax
>>> all(L[1:])
True
>>> sum(L)
15
>>> 
