import math



#global variables

rear = -1
size = 2
maxSize = 5
maxItems = 2
q1 = [0 for _ in range(0, maxSize)]
front = -1

def isEmpty():
    global size
    if(size == 0):
        return True
    else:
        return False
#endfunc

def isFull():
    global size
    global maxSize
    if size == maxSize:
        return True
    else: 
        return False
    #endif
#endfunc

def enqueue(q1 , item): #my_q):
    global rear 
    global size
    global maxSize
    rear = (rear + 1) % maxSize
    q1[rear] = item # item
    size = size + 1
#end procedure
print(q1)
enqueue(q1 , 5)
print(q1)
enqueue(q1, 6)
print(q1)

def dequeue(q1):
    global front
    global size
    global maxSize
    if isEmpty():
        return 0
    else:
        
        front = (front + 1) % maxSize
        size = size - 1
    return q1[front - 1] 
#endproc