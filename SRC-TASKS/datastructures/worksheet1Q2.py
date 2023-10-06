MAX = 10
name_array = [ "" for _ in range(MAX)]
name_array[0] = "Bob"
name_array[1] = "Bill"
name_array[2] = "Gary"
name_array[3] = "Mitya"
i = 0
found = False
print(name_array)

NameSearch = input("Enter a name to search for: ")
while not found and i < MAX:

    if name_array[i] ==  NameSearch:
        print("It has been found ")
        found = True
        i += 1
    else:
        print("Not found try again ")
        NameSearch = input("Enter a name to search for: ")
        i += 1
    #endif
#endwhile
if found:
    print(i)
else:
    print("Not found")
#endif