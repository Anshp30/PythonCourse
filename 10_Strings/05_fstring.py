#String Formatting

template = "Dear {},You are Awesome.Take This {}$  Bag."

a = "john"
a1= 10000
b = "alice"
b1= 5000
c = "Bob"
c1= 3000

s1=template.format(a,a1)
print(s1)

print(f"Dear {a},You are awesome.take this {a1}$ bag.") 
print(f"Dear {b},You are awesome.take this {b1}$ bag.") 
print(f"Dear {c},You are awesome.take this {c1}$ bag.") 



name = "Ansh"
age = 20

print(f"My Name is {name},I am {age} Year Old!!")

x = 10
y = 5

print(f"The sum of {x} and {y} is {x+y}")

text = "python"
print(f"{text:<10}") # Left Align 
print(f"{text:>10}") # Right Align
print(f"{text:^10}") # Cente Align