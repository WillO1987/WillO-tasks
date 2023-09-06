running = True #creates booleon var
while running == True: #while loop
    option = input(int("Enter your an number between 1 and 3")) # asks user to pick between 1 and 3 
    if option >=1 and option <= 3: #if statement making sure between 1 and 3
        print("You have selcted option number" , option) # if it is prints choice
        running = False #ends while loop
    else:
        print("Wrong try again") #else prints this and the while loop loops round again
    #endif
#endwhile

