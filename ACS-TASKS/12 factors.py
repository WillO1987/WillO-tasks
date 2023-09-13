first_int = int(input("Enter an integer: ")) #asks user to input

factorlist = [] # empty array

for i in range(2 , first_int + 1): # loops round from 2 to the input unmber 
    if first_int % i == 0: # checks for no rmaineder from division 
        factorlist.append(first_int) # if there is no remainder then it is a factor of the number


print ("the factors are" , factorlist) # prints it out 