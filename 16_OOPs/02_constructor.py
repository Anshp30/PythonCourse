class Employee:
    def __init__(self,salary,Name,Bond):
        self.salary = salary
        self.Name = Name
        self.Bond = Bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The Name of the employee is{self.Name}.Salary is {self.salary},The Bond is for {self.Bond} years")

e1 = Employee(34000,"Jhon Deo",4)
e1.get_info()