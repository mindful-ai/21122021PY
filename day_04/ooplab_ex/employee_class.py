class Employee:

    # data: name, age, company, salary, netsalary, tax, hike
    # constructor: name, age, company, salary
    def __init__():
        pass

    # functions
    def printinfo():
        pass

    def modifydata(): # salary, hike  ex: madifydata('salary', '14000000') madifydata('hike', '14')
        pass

    def calctax(): # calctax('13')
        pass

    def calchike(): #calchike('5')
        pass

from datetime import datetime
class newEmployee(Employee):

    def __init__(self, name, age, company, salary, addr):
        super().__init__(name, age, company, salary)
        self.addr = addr
        self.birthyear = 0

    def printinfo():
        pass

    def getbirthyear():
        t = datetime.now()
        self.birthyear = t.year - self.age
        return self.birthyear


# ----------------------------------------- AD

e1 = Employee('Anil', 34, 'Oracle', '1400000')
e2 = Employee('Sunil', 35, 'Oracle', '1500000')
e3 = Employee('Raj', 35, 'Oracle', '1550000')

employees = [e1, e2, e3]

for emp in employees:
    emp.printinfo()

e1.modifydata('salary', "1600000")
e1.calctax('10')
e2.calctax('10')
e3.calctax('10')
e3.calchike('5')

for emp in employees:
    emp.printinfo()


e3 = newEmployee('Kiran', 35, 'Oracle', '1500000', ' J P Nagar, Bangalore')
print('Birth Year =', e3.getbirthyear())


# Polymorphism test

e = e1
e = e3

e.printinfo()