Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -------------------------- lambda functions

>>> # lambda <input> : <outputs> => <function object>
>>> 
>>> tc = lambda t : t * 1.8 + 32
>>> type(tc)
<class 'function'>
>>> 
>>> tc(100)
212.0
>>> 
>>> 
>>> # -------------------------- map()
>>> 
>>> T = [100, 120, 130, 140, 150]
>>> F1 = []
>>> for t in T:
	F1.append(tc(t))

	
>>> F1
[212.0, 248.0, 266.0, 284.0, 302.0]
>>> F2 = map(tc, T)
>>> list(F2)
[212.0, 248.0, 266.0, 284.0, 302.0]
>>> 
>>> F3 = map(lambda t : t * 1.8 + 32, T)
>>> list(F3)
[212.0, 248.0, 266.0, 284.0, 302.0]
>>> 
>>> 
>>> # ------------------------- filter()
>>> 
>>> S = ['red', 'green', 'blue', 'yellow', 'purple', 'magenta']
>>> F1 = filter(lambda s : len(s) < 5, S)
>>> list(F1)
['red', 'blue']
>>> F1 = filter(lambda s : len(s) >= 5, S)
>>> list(F1)
['green', 'yellow', 'purple', 'magenta']
>>> F2 = filter(lambda s : s[-1] == 'e', S)
>>> list(F2)
['blue', 'purple']
>>> F2 = filter(lambda s : s[-1] != 'e', S)
>>> list(F2)
['red', 'green', 'yellow', 'magenta']
>>> 
>>> # ----------------------------- sort()
>>> 
>>> L = ['zebra', 'ant', 'goat', 'python', 'bear']
>>> L.sort()
>>> L
['ant', 'bear', 'goat', 'python', 'zebra']
>>> L.sort(reverse=True)
>>> L
['zebra', 'python', 'goat', 'bear', 'ant']
>>> L.sort(key=lambda i : i[-1])
>>> L
['zebra', 'python', 'bear', 'goat', 'ant']
>>> 
>>> L = [('apples', 3), ('pineapple', 1), ('banana', 2)]
>>> L.sort()
>>> L
[('apples', 3), ('banana', 2), ('pineapple', 1)]
>>> L.sort(key=lambda t : t[1])
>>> L
[('pineapple', 1), ('banana', 2), ('apples', 3)]
>>> L.sort(key=lambda t : t[1], reverse=True)
>>> L
[('apples', 3), ('banana', 2), ('pineapple', 1)]
>>> 
>>> 
>>> # ------------------------------------------ zip()
>>> 
>>> T1 = ("Anil", "Sunil", "Raj")
>>> T2 = ("Oracle", "Infosys", "Wipro")
>>> zip(T1, T2)
<zip object at 0x0000020717B61888>
>>> list(zip(T1, T2))
[('Anil', 'Oracle'), ('Sunil', 'Infosys'), ('Raj', 'Wipro')]
>>> dict(zip(T1, T2))
{'Anil': 'Oracle', 'Sunil': 'Infosys', 'Raj': 'Wipro'}
>>> 
>>> 
>>> # -- unzipping
>>> 
>>> D = {'Anil': 'Oracle', 'Sunil': 'Infosys', 'Raj': 'Wipro'}
>>> D.keys()
dict_keys(['Anil', 'Sunil', 'Raj'])
>>> D.values()
dict_values(['Oracle', 'Infosys', 'Wipro'])
>>> 
>>> D.items()
dict_items([('Anil', 'Oracle'), ('Sunil', 'Infosys'), ('Raj', 'Wipro')])
>>> list(zip(*D.items()))
[('Anil', 'Sunil', 'Raj'), ('Oracle', 'Infosys', 'Wipro')]
>>> 
>>> 
>>> # --------------------------------- format()
>>> 
>>> 'My name is {} and age is {}'.format('Raj', 35)
'My name is Raj and age is 35'
>>> 'My name is {0} and age is {1}'.format('Raj', 35)
'My name is Raj and age is 35'
>>> 'My name is {1} and age is {1}'.format('Raj', 35)
'My name is 35 and age is 35'
>>> 'My name is {0:10} and age is {1:5}'.format('Raj', 35)
'My name is Raj        and age is    35'
>>> 'My name is {0:>10} and age is {1:<5}'.format('Raj', 35)
'My name is        Raj and age is 35   '
>>> 'My name is {0:^10} and age is {1:^5}'.format('Raj', 35)
'My name is    Raj     and age is  35  '
>>> 'My name is {name:^10} and age is {age:^5}'.format(name='Raj', age=35)
'My name is    Raj     and age is  35  '
>>> 
>>> 
>>> name = 'Sunil'
>>> age  = 35
>>> template = 'My name is {name:10} and age is {age:5}'
>>> template.format(name=name, age=age)
'My name is Sunil      and age is    35'
>>> 
>>> 
>>> D = {'Anil' :35, 'Sunil':36, 'Raj':37 }
>>> for key, value in D.items():
	print(template.format(name=key, age=value))

	
My name is Anil       and age is    35
My name is Sunil      and age is    36
My name is Raj        and age is    37
>>> for key, value in D.items():
	print('My name is ', key, ' and age is ', value)

	
My name is  Anil  and age is  35
My name is  Sunil  and age is  36
My name is  Raj  and age is  37
>>> 
>>> 
>>> template =
SyntaxError: invalid syntax
>>> template = '''
------------- NAME  -------- {name}
------------- AGE   -------- {age}
'''
>>> template.format(name=name, age=age)
'\n------------- NAME  -------- Sunil\n------------- AGE   -------- 35\n'
>>> print(template.format(name=name, age=age))

------------- NAME  -------- Sunil
------------- AGE   -------- 35

>>> # ------------------------------ enumerate()
>>> 
>>> L
[('apples', 3), ('banana', 2), ('pineapple', 1)]
>>> L = ['red', 'green' , 'blue']
>>> enumerate(L)
<enumerate object at 0x0000020717B2AB40>
>>> list(enumerate(L))
[(0, 'red'), (1, 'green'), (2, 'blue')]
>>> 
