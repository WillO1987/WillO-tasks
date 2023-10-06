import math
i = 0
#num = [0,0,0,0,0,0]
num = [0 for _ in range(6)]
total = 0
for i in range(0,6):
    num[i] = int(input("enter Num: "))
    total = total + num[i]
    average = total / len(num)
#next i  
num.reverse()
for i in range(5, -1 , -1):
    print(num[i])
#next i
#num[:: -1] # also reverses 
print("numbers reversed is " , num)
print("Number total is " , total)
print("Numbers average is " , average)

