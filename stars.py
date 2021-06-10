def stars(num):
    for i in range(0, num+1):
        print("*" * i,"\n")
        
num = int(input("Enter the number of steps for the star program: "))
stars(num)
