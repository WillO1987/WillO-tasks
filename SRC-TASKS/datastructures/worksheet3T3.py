class Node:
    def __init__(self, name , pointer):
        self.data = name
        self.pointer = pointer
    #end constructor

    def __repr__(self) -> str:
        return " |Data: "  + self.name + "   Ptr: " + str(self.pointer) + "| "
    

    def orderOutput(self):
        print(self)
#end node record

myList = [Node(" ", -1) for _ in range(50)]

for index in range(0,49):
    myList[index].pointer = index + 1
#next index
myList[49].pointer = None


start_pointer = 1
nextfree = 3

def printOrder(Mylinkedlist):
    global start_pointer
    Current_pointer = start_pointer
    while Current_pointer != -1:
        print(Mylinkedlist[Current_pointer].name)
        Current_pointer = Mylinkedlist[Current_pointer].pointer
    #next current_pointer
#printOrder(linked_list_data)


def AddItem(newItem):
    #check if list is full and if so, print error message
    if nextfree == None:
        print("Error")
    else:
        newName = myList[nextfree].name
        if start == None:
            temp = myList[nextfree].pointer       #save pointer
            myList[nextfree].pointer = None
            start = nextfree
            nextfree = temp
        else:
            p = start
            if newName < myList[p].name:  
                start  = myList[nextfree].pointer
                start = nextfree
            else:   
                placeFound = False    #general case
                while myList[p].pointer != None and placeFound == False:
                    #peek ahead
                    if newName >= myList[myList[p].pointer].name:
                        p = myList[p].pointer
                    else:
                        placefound = True
                    
                
                temp = nextfree
                nextfree = Node[nextfree].pointer
                Node[temp].pointer = Node[p].pointer
                Node[p].pointer = temp
            
        
    
