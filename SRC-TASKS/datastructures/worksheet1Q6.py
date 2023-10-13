rows, cols = (6, 10)
arr = [['empty ' for i in range(cols)] for j in range(rows)]
for row in arr:
    for x in row:
        print(x, end=' ')
    print()
system = True
while system is True: #loops forever until cancelled
    car_row = int(input("Enter the row you parked in: "))
    car_row = car_row - 1
    car_col = int(input("Enter the col you parked in: "))
    car_col = car_col - 1
    if arr[car_row][car_col] == 'TAKEN ': # checks to see if space is taken
        print("Space already taken.") 
        system = True
    #end if
    
    arr[car_row][car_col] = 'taken, '
    for row in arr:
        for x in row:
            print(x, end=' ')
        print()

    #next row
    question = input("Do you want to continue? y or n: ")
    if question == "y":
        system = True #loops the system again
    else:
        system = False #stops the loop
    #end if  



    
