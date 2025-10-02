###############################################################################
#  Program Name   : ex11.py
#  Author         : Liam Naylor
#  Task           : Find the biggest number in a list
###############################################################################

# Create a list of numbers

aList = [1, 5, 7, 11, 9]

largest = 0

# Ask if the numbers in the list are bigger than the current largest number, if they are, replace the current largest number with this number

for number in aList:
    if number > largest:
        largest = number

# Print the largest number

print(largest)  
