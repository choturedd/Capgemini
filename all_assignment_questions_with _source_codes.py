# find the area of rec using the inpu type conversion and formatting string(assignment)
# length=input("enter the length of the rectangle:")
# length=int(length)
# breadth=input("enter the length of the breadth:")
# breadth=int(breadth)
# area=length*breadth
# print(f"the area of rectangle is:{area}")


#assignment: calculate the total amount and quantity as input from the user 
# amount=int(input())
# quantity=int(input())
# add_=lambda amount,quantity:amount*quantity
# print(add_(amount,quantity))

# 1) convert the prices in USD & Euro using appropriate function
#     PricesList_inr =[3000,56000,45000,2300]
#asignment questions
# priceList_inr=[3000,56000,45000,2300]
# usd=map(lambda x:x/86.43,priceList_inr)
# euro=map(lambda x:x/90.43,priceList_inr)
# print(list(usd))
# print(list(euro))


# class Employee:
#     def __init__(self,name,salary,gender):
#         self.name=name
#         self.salary=salary
#         self.gender=gender
#     def show(self):
#          print(f"your name:{self.name}\ngender:{self.gender}\nsalary:{self.salary}")
#     def employee_gen_male(self):
#         # male=[]
#         for i in range(n):
#            if employees[i].gender=='male':
#             #  male.append(employee)
#             #  print(male)
#                  print(f"your name:{employees[i].name}\ngender:{employees[i].gender}\nsalary:{employees.salary}")

#     def employee_gen_fem(self):
#         female=[]
#         if gender=='female':
#             female.append(employee)
#             print(female)
#             #print(f"your name:{self.name}\ngender:{self.gender}\nsalary:{self.salary}")


# n=int(input('enter no.of employees:'))
# employees=[]
# female=[]
# for i in range(n):
#     print(f'\nenter details for employee {i+1}:')
#     name=input('enter name:')
#     gender=input('gender:')
#     salary=float(input('salary:'))
#     employee=Employee(name,salary,gender)
#     employees.append(employee)
# nn=int(input('choose\n1.to print male employee list\n2.to print female employee list\n'))
# for i in range(n):
#     if nn==1:
#         employee.employee_gen_male()
        
#     else:
#         employee.employee_gen_fem()


#assignment

# class Emails:
#     def send(self):
#         print('hi, your current message is being forwarded')
# class SMS:
#     def send(self):
#         print("you've recieved a new message")
# class Push:
#     def send(self):
#         print('push mesaage has been enabled')
# def func(obj):
#      obj.send()
# email=Emails()
# func(email)
# sms=SMS()
# func(sms)
# push=Push()
# func(push)


#assignment
# from abc import ABC,abstractmethod
# class Notification(ABC):
#     @abstractmethod
#     def myabstractmethod(self):
#         pass
#     def disp(self):
#         print('concrete method')
# def func(obj):
#     obj.send()
# class Email(Notification):
#     def myabstractmethod(self):
#         print('email notification')
#     def send(self):
#         print("Your email has been forwarded")
# class Sms(Notification):
#     def myabstractmethod(self):
#         print('SMS notification')
#     def send(self):
#         print("You've received a SMS")
# class Push(Notification):
#     def myabstractmethod(self):
#         print('Push notification')
#     def send(self):
#         print("Your message was pushed into rsc Chat")
# email=Email()
# func(email)  
# sms=Sms()
# func(sms)
# push=Push()
# func(push)

# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def work():
#         pass
#     def get_salary():
#         pass
# class Employees(ABC):
#     def __init__(self,name,role,salary,department):
#         self.name=name
#         self.role=role
#         self.salary=salary
#         self.department=department
#     @abstractmethod
#     def work():
#         pass
#     def get_salary():
#         pass
#     def show():
#         print('employee class')
# class Manager(Employees):
#     def work(self):
#         print('employee is in manager role')
#     def get_salary(self):
#         return self.salary


# class Developer():
#     def work(self):
#         print('employee is in developer role')
#     def get_salary(self):
#         return self.salary

# class Department(Employees):
#     list_emp=[]
#     def __init__(self, name, role, salary, department):
#         super().__init__(name, role, salary, department)
#     def work(self):
#         print('employee is in developer role')
#     def get_salary(self):
#         return self.salary        
#     def hire(self):
#         self.list_emp.append()

# list_emp=[]
# d=Department('indra','tester',22222,'engineer')
# print(d.hire())


# # products="yogurt eggs cookies cookies eggs yogurt apple yogurt apple"
# # word=products.split()
# # count={}
# # for i in word:
# #     if i in count:
# #         count[i]+=1
# #     else:
# #         count[i]=1

# # print(dict(count))

# sales_data =[
#     {"region": "North", "sales": 15000},
#     {"region": "South", "sales": 8000},
#     {"region": "West", "sales": 7000},
#     {"region": "East", "sales": 5000},
#     {"region": "South", "sales": 12000},
#     {"region": "West", "sales": 7000},
#     {"region": "East", "sales": 5000},
#     {"region": "South", "sales": 12000}
# ]
# reg_sal={}
# for sale in sales_data:
#     region=sale['region']
#     sales=sale['sales']
#     if region in reg_sal:
#         reg_sal[region]+=sales
#     else:
#         reg_sal[region]=sales
# for region,sales in reg_sal.items():
#     print(f'Region:{region},sales:{sales}')
# from collections import Counter
# initial_stock = {"apple": 50,"banana": 100,"orange": 75}

# sold_item = {"apple": 10, "banana": 20, "orange": 15}
# t1=Counter(initial_stock)
# t2=Counter(sold_item)
# cur_stck=t1-t2
# print(dict(cur_stck))
# # i=0
# for i in range(len(initial_stock)):
#     if sold_item.keys()==initial_stock.keys():
#         cur_stck=(initial_stock.values()).difference()
#     print(cur_stck)


# i=0
# res=''
# num=input('enter your number:')

# number_word={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}
# for number in num:
#     if number in number_word:
#         res=res+ number_word[number]
    
#     else:
#         print()
#         # num=number['num']
#         # dig=number['res']
# # for i in range(len(num)):
# print(res)
    # for i in range(len(num)):
    #     if num[i]=='1':
    #          res+='one '
    #     elif num[i]=='2':
    #          res+='two '
    #     elif num[i]=='3':
    #         res+='three '
    #     elif num[i]=='4':
    #         res+='four '
    #     elif num[i]=='5':
    #         res+='five '
    #     elif num[i]=='6':
    #         res+='six '
    #     elif num[i]=='7':
    #         res+='seven '
    #     elif num[i]=='8':
    #         res+='eight '
    #     elif num[i]=='9':
    #         res+='nine '
# for num,dig in res.items():
#     print(f'num:{num},digit:{dig}')

# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     # def show(self):
# class Auth_employee(Employee):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age, salary )
#     def show(self):
#         if 
# n=int(input('enter no.of employees:'))
# emp=[]
# for i in range(n):
#     print(f'employee {i+1}\n')
#     name=input('employee name:')
#     age=int(input('enter age:'))
#     salary=int(input('enter salary:'))
#     employee=Auth_employee(name,age,salary,)
#     emp.append(employee)


# Your task is to design an Employee Management System using Object-Oriented Programming (OOP) principles such as abstraction, inheritance, and polymorphism in Python.
# Instructions:show
# Create an Interface Employee (Abstract Base Class)
# Define an abstract class Employee using the ABC module.
# Include two abstract methods:
# work(self) -> str: Defines the work responsibilities of the employee.
# get_salary(self) -> float: Returns the salary of the employee.
# Implement Concrete Employee Classes
# Create two classes, Manager and Developer, that inherit from Employee.
# Each class should implement the work method to describe the employee’s role.
# Implement the get_salary method to return the salary of the employee.
# Create a Department Class to Manage Employees
# The Department class should store a list of employees.
# Implement methods:
# hire(self, employee: Employee): Adds an employee to the department.
# fire(self, employee: Employee): Removes an employee from the department.
# get_total_salary(self) -> float: Returns the total salary of all employees.
# show_employee_details(self): Displays all employees, their salary, and work description.
# Test the Implementation
# Create instances of Manager and Developer with names and salaries.
# Add them to a Department and display their details.
# Calculate and print the total salary expense.


# from abc import ABC,abstractmethod
# class Employee(ABC):
#     def __init__(self,name,work,salary,department):
#         self.name=name
#         self.work=work
#         self.salary=salary
#         self.department=department
#     @abstractmethod
#     def employee_work(self):
#         pass
#     @abstractmethod
#     def get_salary(self):
#         pass
#     def show0(self):
#         print(f'employee name:{self.name}')
#     def show(self):
#         print(f'employee work:{self.work}')
#     def show1(self):
#         print(f'Employee salary:{self.salary}')
# class Manager(Employee):
#     def __init__(self,name, work, salary,department):
#         super().__init__(name,work, salary,department)
#     def name_emp(self):
#         self.show0()
#     def employee_work(self):
#         self.show()
#     def get_salary(self):
#         self.show1()
#     def depart(self):
#         print(f'department:{self.department}')
# class Developer(Employee):
#     def __init__(self,name, work, salary,department):
#         super().__init__(name,work, salary,department)
#     def name_emp(self):
#         self.show0()
#     def employee_work(self):
#         self.show()
#     def get_salary(self):
#         self.show1()
#     def depart(self):
#         print(f'department:{self.department}')
# class Department(Employee):
#     dev=[]
#     manager=[]
#     def __init__(self,name,work,salary,department):
#         super().__init__(name,work,salary,department)
#     def employee_work(self):
#         self.show()
#     def get_salary(self):
#         self.show1()
#         self.dev=[]
#         self.manager=[]
#     # def employee_work(self):
#     #     return super().employee_work()
#     # def get_salary(self):
#     #     return super().get_salary()
#     # def depart(self):
#     #     return super().depart()
#     def hire(self):

#         print()
#     def show(self):
#         for emp in list_employees:
#            if emp.department.lower()=='developer':
#                 self.dev.append(emp)
#            elif emp.department.lower()=='manager':
#                 self.manager.append(emp)
#         for dev in self.dev:
#             print(f'name:{dev.name},work:{dev.work},salary:{dev.salary},department:{dev.department}')
#         for manager in self.manager:
#             print(f'name:{manager.name},work:{manager.work},salary:{manager.salary},department:{manager.department}')
# n=int(input('enter no.of employees:'))
# list_employees=[]
# for i in range(n):
#     name=input(f'enter name of employee{i+1}:')
#     work=input('enter the employees designation:')
#     salary=float(input('enter the salary of the employee:'))
#     department=input('enter the department:')
#     # employee=Manager(work,salary,department)
#     # list_employees.append(employee)
#     if department=='developer':
#         emp=Developer(name,work,salary,department)
#     elif department=='manager':
#         emp=Manager(name,work,salary,department)
#     list_employees.append(emp)
# rem_or_add=int(input('select the options:\n1.add employee\n2.remove employee\n'))
# if rem_or_add==1:
#     n=int(input('enter no.of employees u wnat to enter:'))
#     for i in range(n):
#         print("Enter the details to be add:")
#         name=input(f'enter name of employee{i+1}:')
#         work=input('enter the employees designation:')
#         salary=float(input('enter the salary of the employee:'))
#         department=input('enter the department:')  
#         add=Department(name,work,salary,department)      
#         list_employees.append(add)
        
# add.show()
# print(add.hire())



# from flask import Flask,request,jsonify
# from flask_cors import CORS
# import mysql.connector
# app=Flask(__name__)
# CORS(app)
# connection=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='Abcd@.1234',
#     database='newapi'
# )
# cursor=connection.cursor()
# @app.route('/apitble',methods=['POST'])
# def new_student():
#     data=request.json
#     student_name=data['student_name']
#     gender=data['gender']
#     age=data['age']
#     department=data['department']
#     section=data['section']
#     grade=data['grade']
#     cursor.execute("insert into apitble(student_name,gender,age,department,section,grade) values (%s,%s,%s,%s,%s,%s)",(student_name,gender,age,department,section,grade))
#     connection.commit()
#     return jsonify({"message":"new user added successfully"}),201
# @app.route('/apitble',methods=['GET'])
# def get_info():
#     cursor.execute("select * from apitble")
#     users=cursor.fetchall()
#     return jsonify(users)
# # @app.route('/apitble/<int:id>', methods=['PUT'])
# # def add_
# @app.route('/apitble/<string:department>', methods=['GET'])
# def get_depwise(department):
#     cursor.execute("select * from apitble where department=%s",(department,))
#     user=cursor.fetchall()
#     if user:
#         return jsonify(user)
#     return jsonify({"message":"user not found"}),404
# @app.route('/apitble/gender/<string:gender>',methods=['GET'])
# def get_genderwise(gender):
#     cursor.execute("select * from apitble where gender=%s",(gender,))
#     userr=cursor.fetchall()
#     if userr:
#         return jsonify(userr)
#     return jsonify({"message":"user not found"}),404
# @app.route('/apitble/count',methods=['GET'])
# def count_students():
#     cursor.execute("select count(*) from apitble")
#     ttl_student=cursor.fetchone()[0]
#     return jsonify({"total student":ttl_student})
# app.run(debug=True)




# 5) You have a list of cities with their population data. Sort the cities in descending order of their population.
#    cities = [
#     {"name": "New York", "population": 8419600},
#     {"name": "Los Angeles", "population": 3980400},
#     {"name": "Chicago", "population": 2716000},
#     {"name": "Houston", "population": 2328000}
# ]
# cities = [
#     {"name": "New York", "population": 419600},
#     {"name": "Los Angeles", "population": 3980400},
#     {"name": "Chicago", "population": 2716000},
#     {"name": "Houston", "population": 2328000}
# ]
# n=sorted(cities,key=lambda index:(-index['population'],(index['name'])))
# print(list(n))


# 3) products = [
#     {"name": "Laptop", "price": 92000},
#     {"name": "Smartphone", "price": 48000},
#     {"name": "Tablet", "price": 20000},
#     {"name": "Monitor", "price": 8000}
#     ]
#     Display the Product in ascending order based on the price of the product
# products = [
#     {"name": "Laptop", "price": 92000},
#     {"name": "Smartphone", "price": 48000},
#     {"name": "Tablet", "price": 20000},
#     {"name": "Monitor", "price": 8000}
#     ]
# n=sorted(products, key=lambda index:(index['price'],index['name']))
# print(list(n))


# 4) You have a list of numbers. Filter out the odd ones, double the even numbers, and sort them in ascending order
# num=[1,2,3,4,5,6,7,8,9]
# odd=filter(lambda x:x%2==0,num)
# n=list(odd)
# n.sort()
# d=map(lambda x:x*2,n)
# print(n)
# print(list(d))



# 2) student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]
#     List the name which has more than 6 characters as lone_names list using appropriate function
# student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]
# l=filter(lambda x:len(x)>6,student_name_list)
# print(list(l))



# 6) Extract Emails of Verified Users
#   You have a list of user records with email and a verification status. Extract the emails of verified users.
# 	users = [
#     {"email": "alice@example.com", "verified": True},
#     {"email": "bob@example.com", "verified": False},
#     {"email": "charlie@example.com", "verified": True},
#     {"email": "daisy@example.com", "verified": False}
# 	 ]
# sers = [
#     {"email": "alice@example.com", "verified": True},
#     {"email": "bob@example.com", "verified": False},
#     {"email": "charlie@example.com", "verified": True},
#     {"email": "daisy@example.com", "verified": False}
# 	 ]
# n=filter(lambda x:x['verified']==True,sers)
# print(list(n))



# 7) Calculate Discounts for Products
#  You have a list of products with their prices. Apply a 20% discount to products costing more than $100 and return the updated prices.

# 	products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Headphones", "price": 80},
#     {"name": "Smartphone", "price": 700},
#     {"name": "Monitor", "price": 150}
#    ]

# list out discounted products
# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Headphones", "price": 80},
#     {"name": "Smartphone", "price": 700},
#     {"name": "Monitor", "price": 150}
#    ]
# n=filter(lambda x:x['price']>100,products)
# nn=list(n)
# print(nn)
# nnn=map(lambda x:x['price']*0.8,nn)
# print(list(nnn))


# 8) sort Words by Length
#   Sort them in ascending order of their lengths.
# 	words = ["apple", "banana", "cherry", "date", "fig"]
# words = ["apple", "banana", "cherry", "date", "fig"]
# asc=sorted(words,key=lambda x:len(x))
# print(asc)



# 9) write a program to remove the duplicates in the list
# numbers3=[2,2,4,6,3,4,6,1]
# numbers3=[2,2,4,6,3,4,6,1]
# d=filter(lambda x:{x},numbers3)
# print(list(set(d)))