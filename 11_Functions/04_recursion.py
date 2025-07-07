# Function Call Itself Is called as Recursion

# #Fibonacci
''' 
0 1 1 2 3 5 8 13 
0 1 2 3 4 5 6.....
fib(0)=0
fib(1)=1
fib(2)=fib(0)+fib(1)
fib(3)=fib(1)+fib(2)
fib(4)=fib(2)+fib(3)
fib(n)=fib(n-2)+fib(n-1)

'''
def fib(n):
    #Base case of Recursion
    if(n==0 or n==1):
        return n
    return fib(n-2)+fib(n-1)
print(fib(6))

fib(4) + fib(5)
fib(2)+fib(3)  + fib(3)+fib(4)
fib(0)+fib(1)+fib(1)+fib(2)  + fib(1)+fib(2)+fib(2)+fib(3) 
0 + 1 + 1 + fib(0)+fib(1) + 1 + fib(0)+fib(1)+fib(0)+fib(1)+fib(1)+fib(2)
0+1+1+0+1+1+0+1+0+1+1+fib(0)+fib(1)
0+1+1+0+1+1+0+1+0+1+1+0+1

# Factiroal 
'''
1! = 1
2! = 2*(2-1)!
3! = 3*(3-1)!
n! = n*(n-1)!
''' 

def fact(n):
    #Base case 
    if n==1:
        return 1 
    return n * fact(n-1)
print(fact(4))

'''
fact(4)= 4* fact(4-1)
       = 4 * fact(3)
       = 4 * 3 * fact(3-1)
       = 4 * 3 * fact(2)
       = 4 * 3 * 2 * fact(2-1)
       = 4 * 3 * 2 * fact(1)
       = 4 * 3 * 2 * 1
       = 24

'''


