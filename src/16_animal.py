"""
abstractmethod : in case you use it, it will not allow to make object from Animal class 
    - will say "Can't instantiate abstract class Animal with abstract methods move, speak"
class : the blueprint
instance : the actual object
"""

class Animal:
    def __init__(self, species, weight, color, name, environment):
        self.species = species
        self.weight = weight
        self.color = color
        self.name = name
        self.environment = environment
    def move(self):
        print(f"???")
    def speak(self):
        print("???")

class Dog(Animal):
    def __init__(self, weight, color, name):
        super().__init__("DOG", weight, color, name, "LAND")
    def speak(self):
        print("woof!")
    def move(self):
        print(f"{self.name} walks")

d = Dog(20, "brown", "Kiki")
d2 = Dog(50, "black", "Mucho")

print('My name is', d.name)
print(d2.speak())

class Cat(Animal):
    def __init__(self, weight, color, name):
        super().__init__("CAT", weight, color, name, "LAND")
    def speak(self):
        print("meow!")
    def move(self):
        print(f"{self.name} jumps!")


c = Cat(20, "silver", "Fatty")
c2 = Cat(50, "gray", "Acid")

print(f'My name is {c.name} and lives in {c.environment}')
print(c2.speak())

a = Animal("DOG", 30, "white", "fido", "LAND")
a2 = Animal("CAT", 30, "yellow", "yellow-cat", "LAND")

print(a.name, a2.name)