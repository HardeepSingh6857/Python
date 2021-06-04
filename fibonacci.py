#Using list data structre
f = [0,1]

for i in range(2,100):
    new = f[i-1] + f[i-2]
    if (new >100):
        break
    f.append(new)
        
    
print(f)

#Fibonacci alternate
a = 0
b = 1
f = 0
print(a, "\n", b)

while(f < 100):
    f = a + b
    a = b 
    b = f
    print(f)
    
