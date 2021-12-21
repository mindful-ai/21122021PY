Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'mississippi'
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'p', 'i', 's', 'm'}
>>> 
>>> 
>>> s1 = set("abcdefgh")
>>> s1
{'d', 'f', 'b', 'a', 'g', 'h', 'c', 'e'}
>>> 'a' in s1
True
>>> 
>>> s2 = {'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'}
>>> s2
{'i', 'f', 'l', 'k', 'g', 'j', 'h', 'e'}
>>> 
>>> 
>>> # ----------------------------- operations
>>> 
>>> s1 & s2
{'e', 'g', 'f', 'h'}
>>> 
>>> s1 | s2
{'i', 'd', 'f', 'b', 'l', 'k', 'a', 'g', 'j', 'h', 'c', 'e'}
>>> s1 ^ s2
{'i', 'd', 'l', 'b', 'k', 'a', 'j', 'c'}
>>> 
>>> 
>>> # ----------------------------- functions
>>> 
>>> s1.add('x')
>>> s1
{'x', 'd', 'f', 'b', 'a', 'g', 'h', 'c', 'e'}
>>> s3 = {'y', 'z'}
>>> s1.update(s3)
>>> s1
{'x', 'z', 'd', 'f', 'b', 'y', 'a', 'g', 'h', 'c', 'e'}
>>> s1.remove('z')
>>> s1
{'x', 'd', 'f', 'b', 'y', 'a', 'g', 'h', 'c', 'e'}
>>> 
>>> 
>>> s1.union(s2)
{'x', 'i', 'd', 'f', 'b', 'y', 'l', 'k', 'a', 'g', 'j', 'h', 'c', 'e'}
>>> s1.intersection(s2)
{'e', 'g', 'f', 'h'}
>>> 
>>> 
>>> dir(s1)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
