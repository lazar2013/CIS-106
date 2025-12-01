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

#main - execution begins here
#instantiate the object
empl1 = Employee('Frank', 'Alvino', 60000.00)

#use the object
#object syntax is object.method
print(empl1.email)
print(empl1.first)
print(empl1.last)
print(empl1.pay)
print(empl1.bonus(0.10))
print(empl1.bonus(0.20))
