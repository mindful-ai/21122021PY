class MyNumbers:

    def __init__(self, max):
        self.maxlimit = max


    def __str__(self):
        return 'This is object of MyNumbers'


    def __repr__(self):
        return 'MyNumber Object with maximum limit ' + str(self.maxlimit)


    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= self.maxlimit:
            x = self.a
            self.a += 1
            return x**2
        else:
            raise StopIteration

myobj = MyNumbers(10)
myiter = iter(myobj)


print(myobj)

for x in myiter:
  print(x)
