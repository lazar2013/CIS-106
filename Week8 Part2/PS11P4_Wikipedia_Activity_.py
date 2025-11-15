#https://en.wikiversity.org/wiki/Programming_Fundamentals/Strings
#Create a program that asks the user for a line of text. Then ask the user for the number of 
#characters to print in each line, the number of lines to be printed, and a scroll direction, 
#right or left. Using the given line of text, duplicate the text as needed to fill the given number 
#of characters per line. Then print the requested number of lines, shifting the entire line's content 
#by one character, left or right, each time the line is printed. The first or last character will be 
#shifted / appended to the other end of the string. For example, if shifting the line to the left:
#   Repeat this. Repeat this. 
#    epeat this. Repeat this. R
#    peat this. Repeat this. Re
#Or if shifting the line to the right:
# Repeat this. Repeat this. 
#     Repeat this. Repeat this.
#    . Repeat this. Repeat this

#Ask user for a line of text
line = input("Enter a movie title:")

#Ask how many characters display per line
line_length = int(input("How many characters do you want to display per line?"))

#Ask how many lines they want to print
number_lines = int(input("Enter the number of lines you want printed:"))

#Ask if they want to scroll left or right
direction = input("Enter the direction you want to scroll (left or right): ")

#Duplicate the text as needed to fill the given number of characters per line
line = line * 3
     
#Print the requested number of lines shifting the entire line's content by one character either 
#left or right each time a line is printed. 
for count in range(number_lines):
    #scroll left
    if direction == "left":
        line = line[1:] + line[0]
        
    #scroll right
    if direction == "right":
        line = line[-1] + line[:-1]

    print(line)