s = "hello world" # Strings are immutable

# s[0]= "V" # You can not do this.

a = len(s)
print(a)

print(s.upper(),s)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

text = " hello world "
print(text.strip()) # output = "hello world"
print(text.lstrip()) # output = "hello world "
print(text.rstrip()) # output = " hello world"

text = "python is fun and fun and fun"
print(text.find("is")) # output = 7
print(text.replace("fun","awesome")) # output = "python is awesome and awesome and awesome "

text = "Apple,Banana,Cherry"
print(text.split(","))
print(",".join(['Apple', 'Banana', 'Cherry']))

text = "python123"
print(text.isalpha()) #output:False
print(text.isdigit()) #output:Fals
print(text.isalnum()) #output:True  # alphanumeric
print(text.isspace()) #output:False

