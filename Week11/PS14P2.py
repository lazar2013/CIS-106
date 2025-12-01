class Student:

    def __init__(self, first, last, dcode, enrolled_credits):
        self.first = first
        self.last = last
        self.dcode = dcode
        self.enrolled_credits = enrolled_credits

    def tuition(self):
        if self.dcode == "I":
            price_per_credit = 250
        else: 
            price_per_credit = 500

        tuition_cost = price_per_credit * self.enrolled_credits
        return tuition_cost

s1 = Student('Lazar', 'Georgiev', "I", 6)
s2 = Student('Tim', 'Jones', "O", 6)

print(s1.first)
print(s1.last)
print(s1.dcode)
print(s1.enrolled_credits)
print(s1.tuition())

print(s2.first)
print(s2.last)
print(s2.dcode)
print(s2.enrolled_credits)
print(s2.tuition())