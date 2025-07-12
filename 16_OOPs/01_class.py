# Class: Class is bueprint or templet. Eg. Name, Age, FatherName, Elective etc

# Object: Specific instance created from templet (class). Eg.Form Which contain the data for John Doe

class employee:
    campany = "HP"

    def get_salary(self): # Self is importent here becuase self is way to reference of object which is being created.
        return 34000  


e =employee()
print(e.get_salary()) 
print(e.campany) 

e2 = employee()
print(e2.get_salary())     


