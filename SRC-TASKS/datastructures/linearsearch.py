

def linearsearch(array, index, end ,item):
    if array[index] == item:
        return index
    elif array[index] != item and index == end:
        return -1
    
    else:
        return linearsearch(array, index + 1, end , item)





array = [3, 4, 5, 6, 7, 8, 9]
item = 3

result = linearsearch(array, 0, len(array)-1 , item)

if result != -1:
    print("item is at  " + str(result))
else:
    print("Not found")