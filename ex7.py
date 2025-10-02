###############################################################################
#  Program Name   : ex7.py
#  Author         : Liam Naylor
#  Task           : Ask for two number, then pick the biggest number out the two
###############################################################################

# Ask the user for two numbers

num1 = int(input("Give me a number: "))
num2 = int(input("Give me another number: "))

# Print out whichever number is the bigger one out of the two

if num1 > num2:
    print(num1, "is the bigger number")
if num1 < num2:
    print(num2, "is the bigger number")
