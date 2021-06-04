#This program prints prime numbers from 1 to 100
print('2\n3\n5\n7')
for i in range(2,100):
    if(i % 2 == 0):
        continue
    elif(i % 3 == 0):
        continue
    elif(i % 4 == 0):
        continue
    elif(i % 5 == 0):
        continue
    elif(i % 7 == 0):
        continue
    elif(i % 9 == 0):
        continue
    else:
        print(i)
