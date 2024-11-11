class Employee:
    def __init__(self, name, role, salary, DoB):
        self.name = name
        self.role = role
        self.salary = salary
        self.DoB = DoB
    def increase_salary(self):
        self.salary= self.salary*1.15
    def calculate_age(self):
        self.age = 2024-self.DoB[6:]

class Manager:
    def __init__(self, name, role, salary, DoB, bonus):
        self.name = name
        self.role = role
        self.salary = salary
        self.DOB = DOB
        self.bonus = bonus
    def increase_salary(self):
        self.salary= self.salary*1.15
        print(self.name,", your new salary is: £"+self.salary)
    def calculate_age(self):
        self.age = 2024-self.DOB[6:]
    def increase_bonus(self):
        self.bonus=self.bonus*1.1
        print(self.name,", your new bonus is: £"+self.salary)
        
#main
name=input("enter your name")
role=input("enter your role")
salary=int(input("enter salary"))
DoB=input("enter date of birth, DD-MM-YYYY")

