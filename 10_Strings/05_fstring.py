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