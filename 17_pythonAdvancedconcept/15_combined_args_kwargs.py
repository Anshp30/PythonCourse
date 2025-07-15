# *args: Used to pass a variable number of positional arguments to a function. It collects all the extra arguments into a tuple.

# **kwargs: Used to pass a variable number of keyword arguments to a function. It collects all the extra named arguments into a dictionary.
def func1(*args,**kwargs):
    print(args)
    print(kwargs)

func1(1,5,4,6,jeel=34,ansh = 45,sujal=54,sahil=65)