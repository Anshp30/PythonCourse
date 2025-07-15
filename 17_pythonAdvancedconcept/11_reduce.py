from functools import reduce
numbers = [1,2,3,4,5,6]
#         [3,3,4,5,6]
#         [6,4,5,6]
#         [10,5,6]
#         [15,6]
#         [21]

# reduce():Applies a function cumulatively to the elements of an iterable to reduce it to a single value.
def sum(a,b):
    return a+b
c = reduce(sum,numbers)
print(c)
