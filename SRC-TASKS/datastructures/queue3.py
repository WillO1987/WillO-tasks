import math


class Queue:
    def __init__(self):
    
        self.data = []
        self.fp = 0 
        self.rp = -1
        
    #endconstrutor
    # def __repr__(self) -> str:
    #     ptr = self.fp
    #     return_str = ""
    #     while ptr != (self.rp + 1) % self.maxsize:
    #         return_str = str(self.data[ptr]) + " "
    #         ptr = (ptr + 1) % self.maxsize

    #     #endwhile
    #     return return_str
    #endfunc

    def isEmpty(self):
        return len(self.data) == 0
    def enqueue(item, self):
        self.data.append(item) # adds to the LIST
    def dequeue(self):
        if self.isEmpty(self):
            return 0
        else:
           
            return self.data.pop(0)
#endclass

q1 = Queue()
q2  = Queue()

print(q1.data)
for num in range(11,15):
    Queue.enqueue(num, q1)
#endfor
print(q1.data)
print(q1)
print(q2.data)
for num in range(101,105):
    Queue.enqueue(num, q2)
#endfor

print(q2.data)

print(q2)