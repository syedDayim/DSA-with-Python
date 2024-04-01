# Write a function to print first N natural numebers:

"""
1 2 3 4 5 6 7 8 9
"""


def printNum(number):
    if number > 0:
        printNum(number - 1)
        print(number)


printNum(5)