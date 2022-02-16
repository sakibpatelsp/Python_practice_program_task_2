'''write a program to find area of rectangle and square using polymorphism'''
class Area: #class
    def find_area(self, a=None, b=None): #function
        if a != None and b != None:
            print("Rectangle:", (a * b))
        elif a != None:
            print("square:", (a * a))
        else:
            print("No figure assigned")
obj1=Area() #object
obj1.find_area() #function call
obj1.find_area(10) #function call
obj1.find_area(10,20) ##function call