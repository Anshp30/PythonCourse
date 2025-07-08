#Positional argument 

def add(a,b,plus=0):
    x = a + b + plus
    return x

c = add(4,3,3)
print(c)

#Default argument

def greet(name="Ansh"):
    return f"Hello,{name}!"
print(greet())

#Keyword argument 

def student(name,age):
    return f"Name:{name} , Age:{age}"
print(student(age = 20, name = "Ansh"))

