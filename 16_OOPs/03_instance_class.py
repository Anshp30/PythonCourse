class Employee:
    company = "Asus"  # This is class attribute.
    def __init__(self,salary,Name,Bond,company):
        self.salary = salary
        self.Name = Name
        self.Bond = Bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The Name of the employee is{self.Name}.Salary is {self.salary},The Bond is for {self.Bond} years")

e1 = Employee(34444,"Jhon",3, "Tesla")
print(e1.company) # Will Always print instance attribute whenever present
print(Employee.company) # This is always print class attribute because name of the class are written.

# Object introspection

print(dir(e1))
