# ------------class And Object-----------------------------------------------------------------------

# class Creation():
#     a=10
#     b=20
# c1=Creation()

#  ---------------------acessing object and class member------------------------------------------
# class Creation():
#     a=10
#     b=20
# demo1=Creation()
# demo2=Creation()
# print(Creation.a,Creation.b)
# print(demo1.a,demo1.b)
# print(demo2.a,demo2.b)

# ---------------------------------------------------------------------------------
# class School:
#     sname="AJPatel"
#     Sid=307
#     loc="Navsari"
#     time="9 to 5"

# s1=School()
# print(School.sname,School.Sid,School.loc,School.time)
# print(s1.sname,s1.Sid,s1.loc,s1.time)

# -------------------------------------------------------------------------------------------------
# class School:
#     sname="AJPatel"
#     Sid=307
#     loc="Navsari"
#     time="9 to 5"

# s1=School()
# s1.name="SDJ"
# s1.ID="12"
# s1.time="7 to 12"

# s2=School()
# s2.name="ABJ"
# s2.ID="1214"
# s2.time="7 to 3"

# print(s1.name,s1.ID,s1.time)
# print(s2.name,s2.ID,s2.time)

# ----------------------------------------------------------------Method __init__ ------------------------------
# class School:
#     def __init__(self,name,sid,loc,time):
#         self.NAME=name
#         self.SID=sid
#         self.LOC=loc
#         self.TIme=time

# s1=School("AB",15,"surat","9:30 to6:30")
# print(s1.NAME,s1.SID,s1.LOC,s1.TIme)

# -----------------------------------------------------------------------Object method------------------------------
# class School:
#     SNAME="jes"
#     LOC ="Mumbai"
#     PRINCIPLE="Ansh"
#     TIMING='9am to 3pm'

#     def __init__(self,name,sid,age,bg):
#         self.name=name
#         self.sid=sid
#         self.age=age
#         self.bg=bg

        
#     def display(self):
#         print(self.name,self.sid,self.age,self.bg)

#     def dislay_change(self,new_bg):
#         self.bg=new_bg
# s1=School("jeel",7,20,"A ve+")
# s1.dislay_change("O ve-")
# s1.display()

# --------------------------class method -----------------------------------------------------------------------------------

# class School:
#     SNAME="jes"
#     LOC ="Mumbai"
#     PRINCIPLE="Ansh"
#     TIMING='9am to 3pm'


#     @classmethod    
#     def display(cls):
#         print(cls.SNAME,cls.LOC,cls.PRINCIPLE,cls.TIMING)

#     @classmethod
#     def dislay_change(cls,new_bg):
#         cls.bg=new_bg

# School.display()

# -----------------------------Static Method -------------------------------------------------------






# --------------------------SINGLE LEVEL INHERITANCE---------------------------------------------------------------------
# # class A:
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

# class Person:
#     Name = "ANSH"
#     age = 24
#     eduacation ="B.tech"

#     def __init__(self,name,age,education):
#         self.name=name
#         self.age=age
#         self.eduacation=education
    
#     def display(self):
#         print("NAME:",self.name,"AGE:",self.age,"ËDUCATION:",self.eduacation)

#     @classmethod
#     def displaycls(cls):
#         print("NAME:",cls.Name,"AGE:",cls.age,"EDUCATION:",cls.eduacation)
    

# class Teacher(Person):
#       subject="Maths"
#       salary=50000
  
#       def __init__(self,name,age,eduaction,subject,salary):
#         super().__init__(name,age,eduaction)
#         self.subject=subject
#         self.salary=salary
    
#       def display(self):
#         print("SUBJECT:",self.subject,"SALARY:",self.salary)
#         super().display()

#       @classmethod
#       def displaycls(cls):
#         print("SUBJECT:",cls.subject,"SALARY:",cls.salary)
#         super().displaycls()

# a1=Teacher("Jeel",22,"B.tech","Maths",50000)
# a1.displaycls()
              

#----------------------- MULTI LEVEL INHERITANCE-------------------------------------------------------

# class A:
#     a=10

#     def __init__(self,a):
#         self.a=a
        
#     @classmethod
#     def displaycls(cls):
#         print(cls.a)
# class B(A):
#     b=20
#     def __init__(self,b):
#         self.b=b
#     # @classmethod
#     # def displaycls(cls):
#     #     super().displaycls()
#     #     print(cls.b)
# class c(B):
#     c=30  
#     def __init__(self,c):
#         self.c=c
#     # @classmethod
#     # def displaycls(cls):
#     #     super().displaycls()
#     #     print(cls.c)   

# c1=c(c)
# c.displaycls()
# # print(c.mro())


# exercise


# class Employee:
    
#     name="ansh"
#     age=22
#     doj="01-12-2026"
#     salary=50000
        
#     def __init__(self,name,age,doj,salary):  ### constructor
#         self.name=name
#         self.age=age
#         self.doj=doj
#         self.salary=salary
        
#     def display(self): ## object Method
#         print("NAME:",self.name,"AGE:",self.age,"Date Of Join:",self.doj,"SALARY:",self.salary)
               
#     @classmethod  ## class method
#     def displaycls(cls):
#         print(cls.name,cls.age,cls.doj,cls.salary)
    
# class Departement(Employee):
#     department="CSE"
  
#     def __init__(self,name,age,doj,salary,department):
#         self.department=department
#         super().__init__(name,age,doj,salary)

#     def display(self):
#         print("DEPT:",self.department)
#         super().display()

#     @classmethod     
#     def displaycls(cls):
#         print(cls.department)
#         super().displaycls()

# class Manager(Departement):
#     intetive="TZ"
    
#     def __init__(self,name,age,doj,salary,department,intetive):
#         self.intetive=intetive
#         super().__init__(name,age,doj,salary,department)

    
#     def display(self):
#         print("INTE:",self.intetive)
#         super().display()

#     @classmethod
#     def displaycls(cls):
#         print(cls.intetive)
#         super().displaycls()

# a1=Manager("Ansh",24,"01-12-26",50000,"de","aaaa")
# a1.displaycls()

# ------------------------------------Multiple Inheritance---------------------------------------------

# class A:
#     a=10
#     b=20
#     e=45
        
# class B:
#     c=30
#     a=52
   
# class C(B,A):  # Left to rigth inheritance meanse first A than B c>>B>>A
#     d=40
   
# c1=C()
# print(c1.a,c1.b,c1.c,c1.d,c1.e)
# print(C.mro())


#  Create class calculator which is inherting from class add ,class sub ,class div and perform multiple inheritance


# class Add:
#     @staticmethod
#     def add(a,b):
#         print("The output is ",a+b)

# class Sub:
#     @staticmethod
#     def sub(a,b):
#         print("The output is ",a-b)


# class Div:
#     @staticmethod
#     def div(a,b):
#         print("The output is ",a/b)

# class calculator(Add,Sub,Div):
#     pass

# calculator.sub(12,10)
# calculator.add(10,20)
# calculator.div(10,5)


# ---------------------Hierarchichal inheritance-------------------------------

# class Hospital:
#     name="HCG"
#     loc="Ahm"

#     def __init__(self,name,loc):
#         self.name=name
#         self.loc=loc

#     def display(self):
#         print(self.name,self.loc)

# class Employee(Hospital):
#     name="Ansh"
#     dept="nurse"
    
#     def __init__(self,ename,dept):
#         self.ename=ename
#         self.dept=dept
#         super().__init__(ename,id)

#     def display(self):
#         print(self.ename,self.dept)
#         super().display()

# class Patient(Hospital):

#     def __init__(self,pname,id):
#         self.pname=pname
#         self.id=id
#         super().__init__(pname,id)

# a1=Patient()



# EX 2

# class university:
#     university_name="Mumbai"
#     head1="mr.subh"

#     def __init__(self,uid,name,mailid,contactno):
#         self.uid=uid
#         self.name=name
#         self.mailid=mailid
#         self.contactno=contactno
    
#     def display(self):
#         print(self.uid,self.name,self.mailid,self.contactno)

#     @classmethod
#     def displaycls(cls):
#         print(cls.university_name,cls.head1)

# class stxaviour(university):
#       college_name="RNG"
#       head2="latesh"

#       def __init__(self, uid, name, mailid, contactno,stxid):
#           self.stxid=stxid
#           super().__init__(uid, name, mailid, contactno)

#       def display(self):  
#           print(self.stxid)
#           return super().display()
      
#       @classmethod
#       def displaycls(cls):
#           print(cls.college_name,cls.head2)
#           super().displaycls()


# s1=stxaviour(15,"Ansh","pansh@gmail.com",8530831552,"stx2")
# # s1.displaycls()
# s1.display()
          
       
# --------------------------Hybride Inheritance------------------------------
# class A:
#     a=10
#     b=20
# class B(A):
#     c=30
#     d=40
# class C(A):
#     e=50
#     f=60
# class D(B,C):
#     g=70
#     h=80    
# d1=D()
# print(d1.a,d1.b,d1.c,d1.d,d1.e,d1.f,d1.g,d1.h)
# print(D.mro()) 


# ##### ------------------Encapsulation------------------------------

# class Bank:
#     __bmanager="Ramesh"
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance    
# c1=Bank("Ansh",50000)
# # c1.__balance=100000
# # print(c1.name)
# # print(c1.__balance)
# Bank.bmanager="Suresh"
# print(Bank._bmanager)  