

def SumOfOddNautralNumbers(num):
    if num == 1:
        return 1
    else:
        if (num % 2 != 0):
            return num + SumOfOddNautralNumbers(num - 1)
        else:
            return SumOfOddNautralNumbers(num - 1)



print(SumOfOddNautralNumbers(20))