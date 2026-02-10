# class A:
#     a=10
#     b=20
# class B(A):
#     a="I am from class B" 
# b1=B()
# print(b1.a,b1.b)

# from typing import override


# class Bank:
#     Bname="SBI"
#     Branch="Mumbai"
#     Manager="Ramesh"

#     def __init__(self,name,accno,mobileno):
#         self.name=name
#         self.accno=accno
#         self.mobileno=mobileno
        
        
#     def display(self):
#         print("Name:",self.name)
#         print("Account No:",self.accno)
#         print("Mobile No:",self.mobileno)

#     @classmethod
#     def displaycls(cls):
#         print("Bank Name:",cls.Bname)
#         print("Branch:",cls.Branch)
#         print("Manager:",cls.Manager)

#     def change_mobile_no(self,new_mobileno):
#         self.mobileno=new_mobileno

# class Updated_bank(Bank):
    
#     def __init__(self,name,accno,mobileno,adhar,pan,ifsc_code):
#         super().__init__(name,accno,mobileno)
#         self.adhar=adhar
#         self.pan=pan
#         self.ifsc_code=ifsc_code

#     def display(self):
#         super().display()
#         print("Adhar No:",self.adhar)
#         print("PAN No:",self.pan)
#         print("IFSC Code:",self.ifsc_code)

#     def displaycls(cls):
#         print("IFSC Code:",cls.ifsc_code)
#         super().displaycls()
    
# c1=Updated_bank('Ansh',1234567890,9876543210,123456789012,'PAN123456789','SBI0001234')
# c1.display() 
# Updated_bank.displaycls()

# c1.change_mobile_no(1234567890)
# c1.display()

# Create a class father and implement 3 class memebers inherting properties to son child class. and also implement constructor chnaning inside the child class.

# class Father:

#     Name="Anshul"
#     age=50
#     profession="Businessman"


#     def __init__(self,name,age,profession):
#      self.name=name 
#      self.age=age
#      self.profession=profession  

#     def display(self):
#        print("Name:",self.name)
#        print("Age:",self.age)
#        print("Profession:",self.profession) 

# class son(Father):
#     def __init__(self, name, age, profession,school,grade):
#       super().__init__(name, age, profession)
#       self.school=school
#       self.grade=grade

#     def display(self):
#        print("School:",self.school)
#        print("Grade:",self.grade)
#        return super().display()
   
# s1=son("Jeel", 22, "student","AB High School","A++")
# s1.display()


# Create a class person which consist of three object members and two class members and create a another class teacher ehich is inherting from class person and aslo implement constructor chaining and method channing in the example.

class Person:
    Name = "ANSH"
    age = 24
    eduacation ="B.tech"

    def __init__(self,name,age,education):
        self.name=name
        self.age=age
        self.eduacation=education
    
    def display(self):
        print("NAME:",self.name,"AGE:",self.age,"ËDUCATION:",self.eduacation)

    @classmethod
    def displaycls(cls):
        print("NAME:",cls.Name,"AGE:",cls.age,"EDUCATION:",cls.eduacation)
    

class Teacher(Person):
      subject="Maths"
      salary=50000
  
      def __init__(self,name,age,eduaction,subject,salary):
        super().__init__(name,age,eduaction)
        self.subject=subject
        self.salary=salary
    
      def display(self):
        print("SUBJECT:",self.subject,"SALARY:",self.salary)
        super().display()

      @classmethod
      def displaycls(cls):
        print("SUBJECT:",cls.subject,"SALARY:",cls.salary)
        super().displaycls()

a1=Teacher("Jeel",22,"B.tech","Maths",50000)
a1.displaycls()
              

      