class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def sit(self):
        print(f"{self.name} of age {self.age} is sitting.")

    def roll_over(self):
        print(f"{self.name} of age {self.age} is rolling over.")

d1=Dog('x',6)
d1.sit()
d1.roll_over()
