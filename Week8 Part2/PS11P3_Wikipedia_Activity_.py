#https://en.wikiversity.org/wiki/Programming_Fundamentals/Strings
#Problem 3:
#Create a program that asks the user for a line of comma-separated-values. It could be a sequence of
#test scores, names, or any other values. Use string functions/methods to parse the line and print out
#each item on a separate line. Remove commas and any leading or trailing spaces from each item when 
#printed.

#Prompt user
line = input("Enter 5 fruits and seperate them with commas:")

#split fruits into separate parts where there are commas
fruits = line.split(",")

#loop through each fruit in the list, clean up spacing, and print each fruit on its own line
for fruit in fruits:
    clean_fruit = fruit.strip()
    print(clean_fruit)