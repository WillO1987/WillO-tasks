class Node:
    def __init__(self, name, pointer):
        self.name = name
        self.pointer = pointer

    def __repr__(self) -> str:
        return " |Data: " + self.name + "   Ptr: " + str(self.pointer) + "| "

    def orderOutput(self):
        print(self)

myList = [Node("", -1) for _ in range(5)]

for index in range(0, 4):
    myList[index].pointer = index + 1

myList[4].pointer = -1

start = 0
nextfree = 0

def printOrder(Mylinkedlist):
    global start
    Current_pointer = start
    while Current_pointer != -1:
        print(Mylinkedlist[Current_pointer].name)
        Current_pointer = Mylinkedlist[Current_pointer].pointer

def AddItem(newName):
    global nextfree
    global start
    if nextfree == -1:
        print("Error")
    else:
        myList[nextfree].name = newName

        if start == -1 or newName < myList[start].name:
            temp = myList[nextfree].pointer
            myList[nextfree].pointer = start
            start = nextfree
            nextfree = temp
        else:
            p = start
            placeFound = False
            while myList[p].pointer != -1 and not placeFound:
                if newName >= myList[myList[p].pointer].name:
                    p = myList[p].pointer
                else:
                    placeFound = True

            temp = nextfree
            nextfree = myList[nextfree].pointer
            myList[temp].pointer = myList[p].pointer
            myList[p].pointer = temp

# xItem = input("Enter item to be removed")

def removeItem(XItem):
    global nextfree
    global start
    if start == -1:
        print("list is empty")
    else:
        p = start
        if XItem == myList[start].name:
            start = myList[start].pointer
        else:
            while myList[p].pointer != -1 and XItem != myList[myList[p].pointer].name:
                p = myList[p].pointer

            if myList[p].pointer != -1:
                nextfree = myList[p].pointer
                myList[p].pointer = myList[nextfree].pointer
            else:
                print(f"Item {XItem} not found in the list.")

print(myList)
AddItem("Colin")
print("----------------")
print(myList)
AddItem("Derek")
AddItem("Fred")
AddItem("Trevor")
AddItem("Alan")
print(myList)
printOrder(myList)
removeItem("Trevor")
print(myList)
printOrder(myList)