def sum (a,b):
    print("Hey i am summing")
    c = a+b
    global z # pls modified global z 
    z= 0 # This will refre to a globle z and  not crete local variable 
    return c
z = 3
print(sum(3,12))
print(z)