def sum(a,b):
    # a and b are local variable
    c = a+b
    z = 1 # It careate local variable  called z which is destroy after this function
    return c
z= 8 # z is a globle variable
print(z)
print(sum(4,6))

print(z)