scores = []
total = 0
num = 10
for i in range(1,num):
    input = input("Enter the score: ")
    
    scores[i] = input
    total = total + scores[i]
    if(num >= 13):
        num = 1
    #endif

    if(str(scores[i]) == "x"):
        num = num +1
  
#endfor
print("your total score is: " + total)