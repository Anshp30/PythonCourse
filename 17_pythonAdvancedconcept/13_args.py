def sum(*args):
    # args will be tuple of all the value paased to sum
    total = 0
    for item in args:
        total += item
    return total
    
print(sum(12,5,7,6))
