def fact(num):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    print(f)
    
fact(5)
