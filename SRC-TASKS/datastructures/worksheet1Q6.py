
row = 10
space = 6
arr = []
p = "empty"
carpark = [[p] * row, p for _ in range(space)]
Car_Reg = ["" for _ in range(row)]

spacenotfound = True
while(spacenotfound == True):
    print("Would you like to park a car?")
    park = input()
    if(park == "Yes"):
        print("Enter the row and space:")
        x = input()
        y = input()
           
        if(x > 10 or space > 6):
            print("invalid entry")
            
        if(carpark[x][y] == "empty"):
                
            carpark[x][y] = "space is empty"
            print("Enter the registration number")
            Car_Reg[i] = input()
            i = i + 1
    else:
        print("car is pakred here")
            
        



    
