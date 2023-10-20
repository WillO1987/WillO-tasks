import math


class Queue_data:
    def __init__(self , max_size):
        self.data = [0 for _ in range(max_size)]
        self.size = 0
        self.fp = 0 
        self.rp = -1
        self.maxsize = max_size
    #endconstrutor
#endclass

q1 = Queue_data(6)
q2  = Queue_data(6)

def isEmpty(q):
    return q.size == 0
#endfunc

def isFull(q):
    return q.maxsize == q.size


def enqueue(item, q):
    q.rp = (q.rp + 1) % q.maxsize
    q.size += 1
    q.data[q.rp] = item


def dequeue(q):
    if isEmpty():
        return 0
    else:
        
        q.front = (q.front + 1) % q.maxsize
        q.size = q.size - 1
    return q[q.front - 1] 

print(q1.data)
for num in range(11,15):
    enqueue(num, q1)
#endfor
print(q1.data)