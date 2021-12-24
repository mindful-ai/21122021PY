import shelve

f = shelve.open('mydata.shelf')

metadata = f['meta']
L = f['colorlist']
M = f['matrix']
D = f['name']

f.close()

print(L, type(L))
print(M, type(M))
print(D, type(D))

