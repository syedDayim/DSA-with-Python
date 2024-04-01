# Write a function to print first N natural numebers:


def foo(num):
    if num == 1:
        print(num, end=" ")
    else:
        print(num, end=" ")
        foo(num - 1)


foo(10)