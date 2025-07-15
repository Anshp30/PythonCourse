numbers = [1,2,3,4,5,6]

# def squa're(x):
#     return x * x'
 
#map():Transforms each element in an iterable(list,tuple,set) using a given function.
new = list(map(lambda x:x*x,numbers))
print(new)