# def BinarySearch(aList, itemSought):
#     found = False
#     index = -1
#     first = 0 
#     last = len(aList) - 1
#     while first <= last and found == False:
#         midpoint = (first + last) // 2 
#         if aList[midpoint] == itemSought:
#             found = True
#             return midpoint
#         else:
#             if aList[midpoint] < itemSought:
#                 first = aList[midpoint]+ 1 
#             else:
#                 last = aList[midpoint] -1 
#     #endwhile
#     return index 


def binarySearch(array, x, first, last):

    if last >= first:

        mid = first + (last - first)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, first, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, last)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("item is present at  " + str(result))
else:
    print("Not found")