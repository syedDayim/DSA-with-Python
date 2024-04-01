# Write recursive program to print N Even Numbers


def printOdd(num):

    if num == 2:
        print(num)
    else:
        printOdd(num - 1)
        if(num % 2 == 0):
            print(num)



printOdd(100)



