class Animal: # Parent Class (Superclass)
    location = "Africa"
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Speaking now.....")

class Dog(Animal): # This is how inheritance done in python c
    def speak(self):
        super().speak()  # We are using speak function of the parent class.
        print("WOOF!")
 
class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meoww!")

# a = Animal("Dog")
# a.speak()

d = Dog("Rocky")
print(d.name)
d.speak()
print(d.location)

c = Cat("Billi")
print(c.name)
c.speak()
print(c.location)
