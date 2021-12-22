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
        print("\n")
        print('parent class')
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
        


    def calcavg(self):
        self.avg = sum(self.marks.values())/4

    def setrank(self, rank):
        self.rank = rank

    def setmarks(self, sub, marks):
        if sub in ['phy', 'chem', 'math', 'bio']:
            if(type(marks) == int):
                self.marks[sub] = marks
                self.calcavg()

class extstudent(student):
    
    def __init__(self, n, a, c):
        super().__init__(n, a, c)


class extstud(student):

    def __init__(self, n, a, c, hobbies):
        super().__init__(n, a, c)
        self.hobbies = hobbies
        self.cls = 'C'

    def calccls(self):
        if(self.avg > 90):
            self.cls = 'A+'
        elif(80 < self.avg <= 90):
            self.cls = 'A'
        elif(70 < self.avg <= 80):
            self.cls = 'B+'
        elif(50 < self.avg <= 70):
            self.cls = 'B'
        else:
            self.cls = 'C'

    
    def printreport(self): 
        print('child class')
        super().printreport()
        print('----------------------------')
        print('HOBBIES    :', self.hobbies)
        print('CLASS      :', self.cls)
    



# ----------------------------------------------- Application Developer

s1  = extstudent('Anil', 12, '7')

s1.setmarks('phy', 99)
s1.setmarks('chem', 97)
s1.setmarks('math', 97)
s1.setmarks('bio', 93)
s1.setrank(3)

s1.printreport()



s2  = extstud('Anil', 12, '7', ['Cricket', 'Music', 'Movies'])

s2.setmarks('phy', 99)
s2.setmarks('chem', 97)
s2.setmarks('math', 97)
s2.setmarks('bio', 93)
s2.setrank(2)
s2.calccls()

s2.printreport()

# ------------------- Polymorphism

a1 = student('Anil', 12, '7')
a2 = extstud('Sunil', 12, '7', ['Criket'])




# ----------------------- front end developer


a = a2
a.printreport() # polymorphic