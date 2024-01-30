


arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
def swap( x , y , array):
    temp1 = array[x]
    
    array[x] = array[y]
    array[y] = temp1
   
def quicksort(arr):
    listpointer = 0
    pivotpointer = len(arr) - 1
    direction = 1

    while listpointer != pivotpointer:
        if((direction == 1 and arr[listpointer]> arr[pivotpointer]) or (direction == -1 and arr[listpointer]< arr[pivotpointer])):
            swap(listpointer, pivotpointer, arr)
            listpointer, pivotpointer = pivotpointer , listpointer
            direction = direction * -1
    
           
        else:
            listpointer += direction
    
    return pivotpointer
        


def quicksortrec(arr, left, right):
    if left >= right:
        pass
    else:
        pivotpos = swap( left, right, arr)
        quicksortrec(arr, left, (pivotpos - 1))
        quicksortrec(arr, (pivotpos +1) , right)




print(quicksortrec(arr, 0 , len(arr) - 1))
