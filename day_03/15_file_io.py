Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -------------------------- File Operations : Text files
>>> 
>>> # open(), close()
>>> # Read: read(), readline(), readlines()
>>> # Write: write(), writelines()
>>> # tell(), seek()
>>> 
>>> path = "C:\Users\Purushotham\Desktop\oralcepy\day_03\data.txt"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
>>> path = "c:\new\read\text\anchor.dat"
>>> print(path)
c:
ewead	extnchor.dat
>>> path = r"c:\new\read\text\anchor.dat" # raw string
>>> print(path)
c:\new\read\text\anchor.dat
>>> path = r"C:\Users\Purushotham\Desktop\oralcepy\day_03\data.txt"
>>> 
>>> 
>>> f = open(path, 'r')
>>> # modes: r, w, a, b
>>> type(f)
<class '_io.TextIOWrapper'>
>>> f
<_io.TextIOWrapper name='C:\\Users\\Purushotham\\Desktop\\oralcepy\\day_03\\data.txt' mode='r' encoding='cp1252'>
>>> 
>>> d = f.read()
>>> d
'Return a new array of bytes. The bytearray class is a mutable sequence of integers in the \nrange 0 <= x < 256. It has most of the usual methods of mutable sequences, described in \nMutable Sequence Types, as well as most methods that the bytes type has, \nsee Bytes and Bytearray Operations.'
>>> type(d)
<class 'str'>
>>> print(d)
Return a new array of bytes. The bytearray class is a mutable sequence of integers in the 
range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in 
Mutable Sequence Types, as well as most methods that the bytes type has, 
see Bytes and Bytearray Operations.
>>> d.upper()
'RETURN A NEW ARRAY OF BYTES. THE BYTEARRAY CLASS IS A MUTABLE SEQUENCE OF INTEGERS IN THE \nRANGE 0 <= X < 256. IT HAS MOST OF THE USUAL METHODS OF MUTABLE SEQUENCES, DESCRIBED IN \nMUTABLE SEQUENCE TYPES, AS WELL AS MOST METHODS THAT THE BYTES TYPE HAS, \nSEE BYTES AND BYTEARRAY OPERATIONS.'
>>> 
>>> f.read()
''
>>> len(d)
289
>>> f.tell()
292
>>> f.seek(0)
0
>>> f.tell()
0
>>> 
>>> 
>>> f.read(10)
'Return a n'
>>> f.read(10)
'ew array o'
>>> f.read(10)
'f bytes. T'
>>> 
>>> f.seek(0)
0
>>> f.readline()
'Return a new array of bytes. The bytearray class is a mutable sequence of integers in the \n'
>>> f.readline()
'range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in \n'
>>> 
>>> 
>>> f.seek(0)
0
>>> f.readline()
'Return a new array of bytes. The bytearray class is a mutable sequence of integers in the \n'
>>> f.readlines()
['range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in \n', 'Mutable Sequence Types, as well as most methods that the bytes type has, \n', 'see Bytes and Bytearray Operations.']
>>> f.seek(0)
0
>>> d = f.readlines()
>>> type(d)
<class 'list'>
>>> d[0]
'Return a new array of bytes. The bytearray class is a mutable sequence of integers in the \n'
>>> d[1]
'range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in \n'
>>> d[-1]
'see Bytes and Bytearray Operations.'
>>> d[::-1]
['see Bytes and Bytearray Operations.', 'Mutable Sequence Types, as well as most methods that the bytes type has, \n', 'range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in \n', 'Return a new array of bytes. The bytearray class is a mutable sequence of integers in the \n']
>>> 
>>> 
>>> f.close()
>>> 
>>> 
>>> path
'C:\\Users\\Purushotham\\Desktop\\oralcepy\\day_03\\data.txt'
>>> path = r"C:\\Users\\Purushotham\\Desktop\\oralcepy\\day_03\\data2.txt"
>>> f = open(pathm 'w')
SyntaxError: invalid syntax
>>> f = open(path, 'w')
>>> f.write("New file\n")
9
>>> f.writelines(['new file\n', 'new file\n'])
>>> f.close()
>>> 
>>> 
>>> f = open(path, 'a')
>>> d
['Return a new array of bytes. The bytearray class is a mutable sequence of integers in the \n', 'range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in \n', 'Mutable Sequence Types, as well as most methods that the bytes type has, \n', 'see Bytes and Bytearray Operations.']
>>> 
>>> D = [s.upper() for s in d]
>>> D
['RETURN A NEW ARRAY OF BYTES. THE BYTEARRAY CLASS IS A MUTABLE SEQUENCE OF INTEGERS IN THE \n', 'RANGE 0 <= X < 256. IT HAS MOST OF THE USUAL METHODS OF MUTABLE SEQUENCES, DESCRIBED IN \n', 'MUTABLE SEQUENCE TYPES, AS WELL AS MOST METHODS THAT THE BYTES TYPE HAS, \n', 'SEE BYTES AND BYTEARRAY OPERATIONS.']
>>> 
>>> f.writelines(D)
>>> f.close()
>>> 
