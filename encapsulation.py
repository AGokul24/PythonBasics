# restrictions on accessing variables and methods directly.

class Base():
    def __init__(self):
        self.a = "DELETE"
        self.c = "DELETE"

class Derived(Base):
    def __init__(self):
        #Base.__init__(self)
        print("Calling the private member of the base class: ")
        print(self.c)

obj1 = Base()
print(obj1.a)
print(obj1.c)

obj2 = Derived()