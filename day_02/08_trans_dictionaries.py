Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # DICTIONARIES
>>> 
>>> D = {'name':'Raj', 'age':35, 'country':'India'}
>>> type(D)
<class 'dict'>
>>> 
>>> D['name']
'Raj'
>>> D['age']
35
>>> D['name'] = 'Rajesh'
>>> D
{'name': 'Rajesh', 'age': 35, 'country': 'India'}
>>> 
>>> D['company'] = 'Oracle'
>>> D
{'name': 'Rajesh', 'age': 35, 'country': 'India', 'company': 'Oracle'}
>>> D.remove('age')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    D.remove('age')
AttributeError: 'dict' object has no attribute 'remove'
>>> D.pop('age')
35
>>> D
{'name': 'Rajesh', 'country': 'India', 'company': 'Oracle'}
>>> 
>>> # ------------------------- important functions
>>> 
>>> 
>>> D.keys()
dict_keys(['name', 'country', 'company'])
>>> D.value()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    D.value()
AttributeError: 'dict' object has no attribute 'value'
>>> D.values()
dict_values(['Rajesh', 'India', 'Oracle'])
>>> D.items()
dict_items([('name', 'Rajesh'), ('country', 'India'), ('company', 'Oracle')])
>>> 
>>> 
>>> # -------------------------
>>> 
>>> for key, value in D.items():
	print(key, ' -----------> ', value)

	
name  ----------->  Rajesh
country  ----------->  India
company  ----------->  Oracle
>>> 
