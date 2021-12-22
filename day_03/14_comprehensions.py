Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ----------------------- COMPREHENSIONS
>>> 
>>> L = []
>>> for i in range(1000):
	if(i % 3 == 0 and i % 5 == 0):
		L.append(i)

		
>>> L
[0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 330, 345, 360, 375, 390, 405, 420, 435, 450, 465, 480, 495, 510, 525, 540, 555, 570, 585, 600, 615, 630, 645, 660, 675, 690, 705, 720, 735, 750, 765, 780, 795, 810, 825, 840, 855, 870, 885, 900, 915, 930, 945, 960, 975, 990]
>>> 
>>> LC = [x for x in range(1000) if (x % 3 == 0 and x % 5 == 0)]
>>> LC
[0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 330, 345, 360, 375, 390, 405, 420, 435, 450, 465, 480, 495, 510, 525, 540, 555, 570, 585, 600, 615, 630, 645, 660, 675, 690, 705, 720, 735, 750, 765, 780, 795, 810, 825, 840, 855, 870, 885, 900, 915, 930, 945, 960, 975, 990]
>>> 
>>> 
>>> # comprehension is a technique to build a collection of values
>>> 
>>> # collection : [], (), {}, {}
>>> 
>>> # [<expr(x)> <loop(x)> <condition(x)>]
>>> # condition is optional
>>> 
>>> 
>>> # Example 1
>>> L = [1, 3, 5, 7, 9]
>>> L1 = [x**2 for x in L]
>>> L1
[1, 9, 25, 49, 81]
>>> 
>>> 
>>> # Example 2
>>> L = list(range(1, 10))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> # [(1, 1, 1), (2, 4, 8).....]
>>> L2 = [(x, x**2, x**3) for x in L]
>>> L2
[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343), (8, 64, 512), (9, 81, 729)]
>>> 
>>> 
>>> # Example 3
>>> L3 = [(x, x**2, x**3) for x in L if x % 2 != 0]
>>> L3
[(1, 1, 1), (3, 9, 27), (5, 25, 125), (7, 49, 343), (9, 81, 729)]
>>> 
>>> 
>>> # Example
>>> L = ['red', 'green', 'blue', 'yellow', 'golden', 'orange', 'brown']
>>> D1 = { key:len(key) for key in L if key[0] in ['g', 'o']}
>>> D1
{'green': 5, 'golden': 6, 'orange': 6}
>>> 
>>> # Example 5
>>> L = [1, 3, 5, 7, 9]
>>> 
>>> # only if 3, 7 raise to power of 2, otherwise values will remain same
>>> 
>>> L1 = (x**2 for x in L if x == 3 or x == 7)
>>> L1
<generator object <genexpr> at 0x0000028F4BCE2A20>
>>> list(L1)
[9, 49]
>>> 
>>> 
>>> L2 = (x**2 if x == 3 or x == 7 else x for x in L)
>>> L2
<generator object <genexpr> at 0x0000028F4BCE29A8>
>>> list(L2)
[1, 9, 5, 49, 9]
>>> 
