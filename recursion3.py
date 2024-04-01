# Write recursive program to print N odd Numbers


def printOdd(num):

    if num == 1:
        print(num)
    else:
        printOdd(num - 1)
        if(num % 2 != 0):
            print(num)



printOdd(11)



