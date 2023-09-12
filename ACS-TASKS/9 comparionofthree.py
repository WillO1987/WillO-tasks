first_int = int(input("Enter an integer: ")) #asks user to input
second_int = int(input ("Enter a integer: "))
third_int = int(input ("Enter a integer: "))

numbers = [first_int, second_int, third_int] # array with numbers

numbers.sort() # sorts teh array lowest first 

numbers.reverse() # reverses the array to put highest first 

print("Sorted arraay highest first: " , numbers)


