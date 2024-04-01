def sq(num):
    if num == 1:
        return 1*1
    else:
        return (num * num) + sq(num - 1)
    
print(sq(100))