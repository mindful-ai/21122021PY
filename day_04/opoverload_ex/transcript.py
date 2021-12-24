C:\Users\Purushotham\Desktop\oralcepy\day_04\opoverload_ex>python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import op_overload
<op_overload.complex object at 0x000002004A17E278>
<op_overload.complex object at 0x000002004A17E320>
<op_overload.complex object at 0x000002004A17E358>
<op_overload.complex object at 0x000002004A17E3C8>
>>>
>>> import complex from op_overload
  File "<stdin>", line 1
    import complex from op_overload
                      ^
SyntaxError: invalid syntax
>>> from complex import op_overload
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'complex'
>>> c = op_overload.complex(3, 4)
>>> c
<op_overload.complex object at 0x000002004A160748>
>>> print(c)
<op_overload.complex object at 0x000002004A160748>
>>>
>>> s = "python"
>>> s
'python'
>>> print(s)
python
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(c)
['__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__weakref__', 'img', 'real']
>>> exit()


----------------------- after implementing __repr__ and __str__

>>> import op_overload
3 + j4
4 + j5
7 + j9
-4 + j-5
>>> c = op_overload.complex(5,6)
>>> c
5 + j6
>>> print(c)
5 + j6


