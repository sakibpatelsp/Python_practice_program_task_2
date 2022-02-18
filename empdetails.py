'''witw a program to print basic details of employee using encapsulation'''


class Employee: # class
    def __init__(self, name, id , salary): #constructor
        self.name = name 
        self.id = id
        self.salary = salary
    def show(self): #function
        print("Name: ", self.name, 'ID is', self.id)
    def sal(self): #function
        print(self.name, 'salary is', self.salary)
emp = Employee('Sakib', 57, 6000) # creating object of a class
emp.show() #function call
emp.sal() #function call