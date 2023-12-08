# name = ['r', 'o' , 'b', 'e','r','t']
# stack = []
# outName = []
# for c in name:
#     stack.append(c)
# for index in range(0,len(stack)):
#     print(stack[-1])
#     outName.append(stack.pop())

# print(outName)

class Stack:
    def __init__(self , size):
        self.data = ['' for _ in range(size)]
        self.maxSize = size
        self.sp = -1
    #end constructor

    def size(self):
        return self.sp + 1
    def isFull(self,):
        return self.size() == self.maxSize
    def isEmpty(self):
            return self.sp - 1 
    def push(self, item):
         if self.isFull():
              print( "is Full")
         else:
            
              self.sp += 1
              self.data[self.sp] = item
        #endif 
    #endprocedure 
    def pop(self):
        if self.isEmpty():
             print( "is empty" ) 
        else:
             temp = self.sp 
             self.sp -= 1
            
             return self.data[temp]
    #endfunction 

    def peak(self):
        if not self.isEmpty():
            return self.data[self.sp]
    #endfunc
myString = input("enter a word")
list1 = list(myString)
numChars = len(list1)
palList = []
s = Stack(numChars)
s.pop()
for c in myString:
    s.push(c)
#next c
s.push("x")
print(s.data)

while not s.isEmpty():
    palList.append(s.pop())

print("".join(palList))

if myString == ''.join(palList):
     print("is a palendrome")
else:
    print("Not a palendrome")