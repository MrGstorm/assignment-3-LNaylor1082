###############################################################################
#  Program Name   : ex10.py
#  Author         : Liam Naylor
#  Task           : Ask for three names, then prints them in a list
###############################################################################

# Ask the user for three friends' names

friend1 = input("Give me a friends name: ")
friend2 = input("Give me another friends name: ")
friend3 = input("Give me yet another friends name: ")

# Puts the names in a list, then prints the names in seperate lines

friendsNames = [friend1, friend2, friend3]

for name in friendsNames:
    print(name)
