#Fibonacci sequence 
a = 1
b = 1
print(a)
print(b)

for x in range(1,21,1): #(start value, stop value + 1, increment value)
    c = a + b
    print(c)
    a = b
    b = c