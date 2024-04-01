def sumNatural(num):
    if num == 1:
        return 1
    return num + sumNatural(num - 1)

print(sumNatural(3))