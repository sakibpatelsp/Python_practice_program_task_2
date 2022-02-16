'''Write a program to illustrate how to overload  + operator'''
 

class Overload: #class
    def __init__(self, a): #constructor
        self.a = a
 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = Overload(10) #object
ob2 = Overload(20) #object
ob3 = Overload("Sakib") #object
ob4 = Overload("Patel") #object
 
print(ob1 + ob2)
print(ob3 + ob4)