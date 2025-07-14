# Decorator is a function that takes the function ,it create a new function inside its body(wrapper). Then its return a new function.

def decorator(func):
    def wrapper():
       print("I am Excuting a function..")
       func()
       print("I have Excute this function...")
    return wrapper

@decorator

def say_hello():
    print("hello!!")

say_hello()


# f = decorator(say_hello)
# f()
'''
f() looking llike this
def f():
       print("I am Excuting a function..")
       print("Hello!!")
       print("I have Excute this function...")

'''
