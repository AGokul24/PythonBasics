
# Child class is derived from the parent class
# Child  class uses the attributes the methods of the parent class
# Improves code reusability - Not need to repeat the same code for further methods.

class student():
    def __init__(self, name, id):
        self.name= name
        self.id = id
    def display(self):
        print(self.name)
        print(self.id)
    def details(self):
        print("The name is "+self.name)
        print("Id : "+self.id)

class FurtherStudentDetails(student):
    def __init__(self,name, id, group, age):
        self.group = group
        self.age = age
        student.__init__(self, name, id)

    def details(self):
        print("The name is " + self.name)
        print("Id : " + str(self.id))
        print("Group : "+self.group)
        print("Age : "+str(self.age))

objStudent = FurtherStudentDetails("Gokul", 23123, "Maths, CSC", 24)

objStudent.details()
objStudent.display()
