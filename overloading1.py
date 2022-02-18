#Program to demonstrate overloading


class Overload1: #class
    def __init__(self, a): #constructor
        self.a = a
 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = Overload1(85) #object
ob2 = Overload1(25) #object
ob3 = Overload1("Sakib") #object
ob4 = Overload1("Patel") #object
print(ob1 + ob2)
print(ob3 + ob4)