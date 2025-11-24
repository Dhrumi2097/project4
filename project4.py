emp=[]
man=[]
dev=[]
class Employee:
        def __init__(self,empid,name,age,salary):
            self.empid=empid
            self.name=name
            self.age=age
            self.salary=salary
            
        def getInfo(self):
            print(f"empid :{self.empid} Name :{self.name} Age :{self.age} Salary:{self.salary}")

class Manager(Employee):
         def __init__(self,manid,name,age,salary,department):
            super().__init__(manid,name,age,salary)
            
            self.department=department
            
         def getInfo(self):
            print(f"manid :{self.manid} Name :{self.name} Age :{self.age} Salary:{self.salary} Department:{self.department}")
    
    
class Developer(Employee):
         def __init__(self,devid,name,age,salary,language):
            super().__init__(devid,name,age,salary)
            self.language=language
            
         def getInfo(self):
            print(f"devid :{self.devid} Name :{self.name} Age :{self.age} Salary:{self.salary} Language:{self.language}")


while True:
      
      print("---Python OOP Project: Employee Management System--- ")
      print()

      print("Choose an operation :")
      print("1. Create a Employee")
      print("2. Create an Manager")
      print("3. Create a Developer")
      print("4. Show Details")
      print("5. Exit")

      choice=int(input("Enter your Choice :"))

      if choice==1:
        id=input("Enter Employee ID (e1,e2):")
        name=input("Enter Employee Name :")
        age=int(input("Enter Employee Age :"))
        salary=int(input("Enter Employee Salary :"))
        print()
        obj=Employee(id,name,age,salary)
        emp.append(obj)
        print("Employee Added Successfully!")

      elif choice==2:
        id=input("Enter Manager ID (m1,m2):")
        name=input("Enter Manager Name :")
        age=int(input("Enter Manager Age :"))
        salary=int(input("Enter Manager Salary :"))
        department=input("Enter Manager's department :")
        print()
        obj1=Manager(id,name,age,salary,department)
        man.append(obj1)
        print("Manager Added Successfully!")

      elif choice==3:
        id=input("Enter Developer ID (d1,d2):")
        name=input("Enter Developer Name :")
        age=int(input("Enter Developer Age :"))
        salary=int(input("Enter Developer Salary :"))
        language=input("Enter Developer's Language :")
        print()

        obj2=Developer(id,name,age,salary,language)
        dev.append(obj2)

        print("Developer Added Successfully!")

      elif choice==4:
        print("Choose Details To show:")
        print()

        print("1. Employee")
        print("2. Manager")
        print("3. Develpor")
        print()

        option=int(input("Enter Your Choice :"))

        if option==1:
            print("Employee Details :")
            for i in emp:
              i.getInfo()

        elif option==2:
            print("Manager Details :")
            for i in man():
                i.getInfo()

        elif option==3:
            print("Developer Details :")
            for i in dev():
                i.getInfo()
           

        else:
            print("Choice is Incorrect !")

      elif choice==5:
          print("Exiting the system. All resources have been freed.")
          print()
          print("Goodbye!")
          break
      else:
          print("Choice is Incorrect!")

            

         
     
        
            
