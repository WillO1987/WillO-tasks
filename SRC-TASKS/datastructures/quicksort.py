
def swap( x , y , array):
    temp1 = array[x]
    
    array[x] = array[y]
    array[y] = temp1
   
def quicksort(arr):
    listpointer = 0
    pivotpointer = len(arr) - 1
    direction = 1

    while listpointer != pivotpointer:
        if arr[listpointer] < arr[pivotpointer]:
            listpointer += direction
        else:
            swap(listpointer, pivotpointer, arr)
            direction = direction * -1


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quicksort(arr)
print(arr)
