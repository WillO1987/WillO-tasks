class Node:
    def __init__(self, name , pointer):
        self.name = name
        self.pointer = pointer
    #end constructor

    def __repr__(self) -> str:
        return " |Data: "  + self.name + "   Ptr: " + str(self.pointer) + "| "
    

    def orderOutput(self):
        print(self)
#end node record

myList = [Node("Empty", -1) for _ in range(5)]

for index in range(0,4):
    myList[index].pointer = index + 1
#next index
myList[4].pointer = -1


start = -1
nextfree = 0

def printOrder(Mylinkedlist):
    global start
    Current_pointer = start
    while Current_pointer != -1:
        print(Mylinkedlist[Current_pointer].name)
        Current_pointer = Mylinkedlist[Current_pointer].pointer
    #next current_pointer
#printOrder(linked_list_data)


def AddItem(newName):
    global nextfree
    global start
    #check if list is full and if so, print error message
    if nextfree == -1:
        print("Error")
    else:
        myList[nextfree].name = newName

        if start == -1:
            temp = myList[nextfree].pointer       #save pointer
            myList[nextfree].pointer = -1
            start = nextfree
            nextfree = temp
        else:
            p = start
            if newName < myList[p].name:  
                start  = myList[nextfree].pointer
                start = nextfree
            else:   
                placeFound = False    #general case
                while myList[p].pointer != -1 and placeFound == False:
                    #peek ahead
                    if newName >= myList[myList[p].pointer].name:
                        p = myList[p].pointer
                    else:
                        placeFound = True
                    
                
                temp = nextfree
                nextfree = myList[nextfree].pointer
                myList[temp].pointer = myList[p].pointer
                myList[p].pointer = temp
print(myList)
# printOrder(myList1)
AddItem("Colin")
# AddItem("Albert",myList1)
# AddItem("Barry",myList1)
print( "----------------")
print(myList)

# printOrder(myList1)
# AddItem("Derek",myList1)
# AddItem("Fred",myList1)
# #outputList(myList)
# AddItem("Trevor",myList1)