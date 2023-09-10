from math import *
valid = False
while valid == False:
    first_int = int(input("Enter an integer between 100 and 199: ")) #asks user to input

    if first_int >= 100 and first_int <= 199: # checks if input is within range 
        valid = True
        
    #endif
    else:
        print("invalid input")
        
#endwhile

hundreds = first_int // 100
tenths = first_int // 10 # whole div
remainder = first_int % 10  # remainder
print( hundreds + "hundreds" + tenths + "tenths and" + remainder + "Remainder") # prints it out
