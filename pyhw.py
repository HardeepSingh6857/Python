operator = int(input("Enter 1, 2, 3, 4: "))
n1 = int(input("Enter no. 1: "))
n2 = int(input("Enter no. 2: "))

if (operator == 1):
  print("answer is: " n1+n2)
elif(operator == 2):
  print("answer is: "n1-n2)
elif(operator == 3):
  print("answer is: "n1*n2)
elif(operator == 4):
  print("answer is: "n1/n2)
else:
  print("invalid operators please enter only 1, 2, 3, 4")
