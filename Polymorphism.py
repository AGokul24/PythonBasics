# Polymorphism - Many forms
# In programming, Same function name but with different signatures

class Cricket():
    def stadiumShape(self):
        print("Stadium shape is Circle")
    def NoofUmpire(self):
        print("Totally 2 umpires")
    def PopularStar(self):
        print("Popular stars : Sachin, Dhoni, Kolhi")

class Football():
    def stadiumShape(self):
        print("Stadium shape is Square, Rectangle")
    def NoofUmpire(self):
        print("Totally 1 umpires")
    def PopularStar(self):
        print("Popular stars : Ronaldo, Messi, Neymer")

CricObj = Cricket()
FootObj = Football()

for Sport in (FootObj,CricObj):
    Sport.stadiumShape()
    Sport.NoofUmpire()
    Sport.PopularStar()