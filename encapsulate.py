'''witw a program to print basic details of student using encapsulation'''
class Student: # class
    def __init__(self, name, roll,branch): #constructor
        self.name = name 
        self.roll = roll
        self.branch = branch
    def show(self): #function
        print("Name: ", self.name, 'Roll No:', self.roll)
    def study(self): #function
        print(self.name, 'is Studying in', self.branch)

# creating object of a class
stud = Student('Sakib', 57, 'Computer Engineering')
stud.show() #function call
stud.study() #function call