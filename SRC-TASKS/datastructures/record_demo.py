import math

#making a record that we cna refrence
class StudentRecord():
    def __init__(self):
        super().__init__()
        self.firstname = ""
        self.Lastename = ""
        self.age = 0
        self.registered = False
    #endconstructorfunction

#
# end class

student1 = StudentRecord()
 # refrencing the record 
student1.firstname = "Dave"
student1.Lastename = "BLOGS"
student1.age = 18
student1.registered = True


student2= StudentRecord()

student2.firstname = "Bob"
student2.Lastename = "smith"
student2.age = 32
student2.registered = False

print(student2.registered)
print(student1.age)

#example of a tuple 

student1t = ("Dave" , "BLOGS" , 18 , True) # orderderd
student1t = ("Bob" , "smith" , 32 , False)

def addone(x):
    x = x +1
    return x
#end func

new_age = addone(student2.age + 1)
print(new_age)
print(student2.age)