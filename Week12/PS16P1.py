#define the object
class Employee: 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # self.rate = 0.0

    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b

class Manager(Employee):
    def __init__(self, first, last, pay):
        super().__init__(first, last, pay)
     
    def long_term_bonus(self):
        bonus = self.pay * 0.40
        return bonus

class Executive(Manager):
    def __init__(self, first, last, pay):
        super().__init__(first, last, pay)

    def executive_bonus(self):
        bonus2 = self.pay * 2.00
        return bonus2

    def long_term_bonus(self):
        bonus =  self.pay * 0.50
        return bonus

#main - execution begins here
#instantiate the object
empl1 = Employee('Frank', 'Alvino', 60000.00)
mgr1 = Manager('Test', 'Employee', 90000.00)
exec1 = Executive('Test', 'Executive', 135000)

#use the object
#object syntax is object.method
print(exec1.email)
print(exec1.first)
print(exec1.last)
print(exec1.pay)
print(exec1.executive_bonus())
print(exec1.long_term_bonus())
