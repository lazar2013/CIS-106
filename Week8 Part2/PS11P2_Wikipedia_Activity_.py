#https://en.wikiversity.org/wiki/Programming_Fundamentals/Strings
#Problem 2:
#Create a program that asks the user for a line of text. Use string functions/methods to delete leading, trailing, and duplicate spaces, and then print the line of text backwards.
#For example:
# the   cat   in   the   hat  
# tah eht ni tac eht
#Use separate subroutines/functions/methods to implement input, each type of processing, and output. Avoid global variables by passing parameters and returning results.

text = input("Enter a line of text:")
    
#Remove extra spaces 
text = text.strip()

#Split words
words = text.split()

#Rejoin words with single spaces
clean_text = " ".join(words)

#Reverse each word
reversed_text = clean_text[::-1]

#Output
print(reversed_text)