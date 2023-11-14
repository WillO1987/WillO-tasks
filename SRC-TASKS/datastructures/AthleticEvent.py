School   = ["AAAA" , "BBBB" , "CCCC", "DDDD"]  

Medal = [4 , 7, 1, 3] 

correct = False
 

while correct == False:

    num = int(input("enter a school number"))
    num1 = num
    
    if num > 4 or num ==  0: 

        correct = False 
        print("Try again: ")
    else:

        if(num == -1):  
            
            # print(num1, School[num1]  , Medal[num1]) 

            correct = True 

        else:

            School_Input = input("enter a school")  

            School[num1] = School_Input 

            Medallswon = input("Enter num of medals") 

            Medal[num1] = Medallswon 

            correct = True 
#endwhile
print(num1, School[num1]  , Medal[num1]) 