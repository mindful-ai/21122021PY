Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LOOPS
>>> for c in 'python':
	print(c.upper(), end='-')

	
P-Y-T-H-O-N-
>>> 
>>> for item in ['red', 'green', 'blue']:
	print(item)

	
red
green
blue
>>> 
>>> print('5', ' X ', '1', ' = ', str(5 * 1))
5  X  1  =  5
>>> for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	print('5', ' X ', i, ' = ', str(5 * i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 30))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> list(range(10, 30, 2))
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
>>> list(range(10, 0, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> for i in range(1, 11):
	print('5', ' X ', i, ' = ', str(5 * i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> # -------------------------------- loop control statements
>>> 
>>> for i in range(1, 11):
	if(i == 5):
		break
	print('5', ' X ', i, ' = ', str(5 * i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
>>> 
>>> 
>>> for i in range(1, 11):
	if(i%3 == 0):
		continue
	print('5', ' X ', i, ' = ', str(5 * i))

	
5  X  1  =  5
5  X  2  =  10
5  X  4  =  20
5  X  5  =  25
5  X  7  =  35
5  X  8  =  40
5  X  10  =  50
>>> 
>>> 
>>> # -------------------------------- while loop
>>> 
>>> i = 1
>>> while i <= 10:
	print('5', ' X ', i, ' = ', str(5 * i))
	i = i + 1

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> # break and continue can be used both in for and while loop structures
>>> 
>>> 
