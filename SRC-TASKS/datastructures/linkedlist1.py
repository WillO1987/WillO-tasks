class Node:
    def __init__(self, data , pointer):
        self.data = data
        self.pointer = pointer
    #end constructor

    def __repr__(self) -> str:
        return " |Data: "  + self.data + "   Ptr: " + str(self.pointer) + "| "
    

    def orderOutput(self):
        print(self)
#end node record

linked_list_data = []
linked_list_data.append(Node("Lucas" , 2))
linked_list_data.append(Node("Ayaan" , 0))
linked_list_data.append(Node("Suren" , -1))
linked_list_data.append(Node("Empty" , 4))
linked_list_data.append(Node("Empty" , -1))

start_pointer = 1
Next_Free = 3

def printOrder(Mylinkedlist):
    global start_pointer
    Current_pointer = start_pointer
    while Current_pointer != -1:
        print(Mylinkedlist[Current_pointer].data)
        Current_pointer = Mylinkedlist[Current_pointer].pointer
    #next current_pointer
printOrder(linked_list_data)
