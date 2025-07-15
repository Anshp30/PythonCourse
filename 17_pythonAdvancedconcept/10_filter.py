# def is_grater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    
a = [1,2,345,78,5,64,69,54,12,7,9,36,77,100,4,6,7]

# Filters elements from an iterable based on a condition.
new = list(filter(lambda x:x>9,a))
print(new)
