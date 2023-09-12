input = input("Enter a time:")
times = input.split(":") # turns input into a array by spliting with :

print(times) # prints out for debugg to check it worked
hourstoseconds = int(times[0]) * 60 * 60 # converts hours to seconds and turns the string into int
minutestoseconds = int(times[1]) * 60 
total = hourstoseconds + minutestoseconds + int(times[2]) # calculates total
print (total , "seconds") #prints results
