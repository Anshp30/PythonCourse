class Employee():
    company = "HP"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    # This Instance method(Default)   
    def print_info(self):
        info = f"The name of employee {self.name} and salary is {self.salary}"
        print(info)

    # static method   
    @staticmethod
    def  sum (a,b):
        return a+b
    
    # class method
    @classmethod
    def print_company(cls):
        print(cls.company)
    
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

e1 = Employee("jack",25000)
e2 = Employee("jeel",35000)
# print(Employee.company)
# print(Employee.name) # this will throw an error
# e1.print_info()
# e2.print_info()

# print(e2.sum(5,5))

print(Employee.company)

e1.change_company("Acer")

print(Employee.company)