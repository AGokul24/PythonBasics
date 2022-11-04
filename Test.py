class MyName:
    AlterName = 'Shawarma'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def voice(self):
        print("My name is "+ self.name)

FirstName = MyName("Gokul", "23")
LastName = MyName("Annadurai", "23")

# print("My fullname is " +FirstName.name +" "+LastName.name)
# print("My nickname is "+ MyName.AlterName)
# print("My age is "+ FirstName.age)

FirstName.voice()
LastName.voice()



