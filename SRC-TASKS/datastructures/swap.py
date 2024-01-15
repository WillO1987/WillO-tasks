array1 = [7 , 4 , 6 , 8 , 1 ,5 ]

def swap( x , y , array):
    temp1 = array[x]
    
    array[x] = array[y]
    array[y] = temp1
   
        

#swap( 0 , 1)
print(array1)
names = ['Sophie', 'Lily', 'Jessica', 'Isabella', 'Ava', 'Poppy', 'Emily', 'Isla', 'Olivia', 'Amelia']

def bubbleSort(arr):
    for i in range(len(arr)-1): # for i = 0 to n - 2
        for j in range(len(arr) - i -1): # for j = 0 to n - i - 2
            if arr[j] > arr[j + 1]:
                swap(j, j + 1 , arr)
            #endif
        #next i
    #next i
#endprocedure
                
bubbleSort(names)
print(names)

    