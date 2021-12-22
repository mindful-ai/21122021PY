class student:

    # Data
    def __init__(self, n, a, c):
        self.name = n
        self.age = a
        self.grade = c
        self.marks = {'phy':0, 'chem':0, 'math':0, 'bio':0}
        self.avg = 0
        self.rank = 0

    # Functions

    def printreport(self):
        print('NAME       :', self.name)
        print('AGE        :', self.age)
        print('GRADE      :', self.grade)
        print('----------------------------')
        print('PHYSICS    :', self.marks['phy'])
        print('CHEMISTRY  :', self.marks['chem'])
        print('MATHS      :', self.marks['math'])
        print('BIOLOGY    :', self.marks['bio'])
        print('----------------------------')
        print('AVERAGE    :', self.avg)
        print('RANK       :', self.rank)
        print("\n")


    def calcavg(self):
        self.avg = sum(self.marks.values())/4

    def setrank(self, rank):
        self.rank = rank

    def setmarks(self, sub, marks):
        if sub in ['phy', 'chem', 'math', 'bio']:
            if(type(marks) == int):
                self.marks[sub] = marks
                self.calcavg()


# ----------------------------------------------- Application Developer

s1  = student('Anil', 12, '7')
s2  = student('Sunil', 12, '8')


s1.printreport()
s2.printreport()

s1.setmarks('phy', 99)
s1.setmarks('chem', 97)
s1.setmarks('math', 97)
s1.setmarks('bio', 93)


s2.setmarks('phy', 99)
s2.setmarks('chem', 96)
s2.setmarks('math', 92)
s2.setmarks('bio', 91)

s1.printreport()
s2.printreport()

if(s1.avg > s2.avg):
    s1.rank = 1
    s2.rank = 2
elif(s1.avg > s2.avg):
    s1.rank = 2
    s2.rank = 1

s1.printreport()
s2.printreport()