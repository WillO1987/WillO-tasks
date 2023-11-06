import math


class Queue_data:
    def __init__(self , max_size):
        self.data = [0 for _ in range(max_size)]
        self.size = 0
        self.fp = 0 
        self.rp = -1
        self.maxsize = max_size
    #endconstrutor
    def __repr__(self) -> str:
        ptr = self.fp
        return_str = ""
        while ptr != (self.rp + 1) % self.maxsize:
            return_str = str(self.data[ptr]) + " "
            ptr = (ptr + 1) % self.maxsize

        #endwhile
        return return_str
    #endfunc
    def isEmpty(self):
        return self.size == 0
    def isFull(self):
        return self.maxsize == self.size
    def enqueue(item, self):
        self.rp = (self.rp + 1) % self.maxsize
        self.size += 1
        self.data[self.rp] = item
    def dequeue(self):
        if Queue_data.isEmpty(self):
            return 0
        else:
        
            self.front = (self.front + 1) % self.maxsize
            self.size = self.size - 1
        return self[self.front - 1] 



    
#endclass

q1 = Queue_data(6)
q2  = Queue_data(7)

# def isEmpty(q):
#     return q.size == 0
# #endfunc

# def isFull(q):
#     return q.maxsize == q.size


# def enqueue(item, q):
#     q.rp = (q.rp + 1) % q.maxsize
#     q.size += 1
#     q.data[q.rp] = item


# def dequeue(q):
#     if isEmpty():
#         return 0
#     else:
        
#         q.front = (q.front + 1) % q.maxsize
#         q.size = q.size - 1
#     return q[q.front - 1] 


print(q1.data)
for num in range(11,15):
    Queue_data.enqueue(num, q1)
#endfor
print(q1.data)
print(q2.data)
for num in range(101,105):
    Queue_data.enqueue(num, q2)
#endfor

print(q2.data)

print(q2)