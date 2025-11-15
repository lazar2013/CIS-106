#https://en.wikiversity.org/wiki/Programming_Fundamentals/Strings
#Problem 1: 
#Create a program that asks the user for a single line of text containing a 
#first name and last name, such as Firstname Lastname. Use string functions/methods 
#to parse the line and print out the name in the form last name, first initial, such 
#as Lastname, F. Include a trailing period after the first initial. Handle invalid 
#input errors, such as extra spaces or missing name parts.

#1. Get first and last name as a single string
long_name = input("Enter First Name and Last Name: ")

#2. Parse the line
name_pieces = long_name.split()
print(name_pieces)

#3. Make first inital of first name capital
first_initial = long_name[:1]
print(first_initial)
first_initial = first_initial.upper()
print(first_initial)

#4. Format as Last name and First initial.
print(name_pieces[1] + ", " + first_initial + ".")