
while True:
    try:
     a = int(input("Enter a Number 1 : "))
     b = int(input("Enter a Number 2 : "))
     print(f"The division of {a/b}")

    except ValueError:
       print("please dont perform bad typecast!")

    except ZeroDivisionError:
       print("Hey dont devide by 0!")

    except Exception as e :
       print("Unknown error occured!", e)


# raise the error !!

# a = int(input("Enter a Number 1 : "))
# b = int(input("Enter a Number 2 : ")) 
# if b==0:
#     raise ValueError("please dont divide by zero!")
# print(f"The division of {a/b}")