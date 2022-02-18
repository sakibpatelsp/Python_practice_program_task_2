'''Write a Program to find area of rectangle square and triangle using inheritance'''

class arearect1:  #baseclass

    def Rect(self,l,b):  #function

        return l*b;  

class areasq2:  #baseclass

    def Sq(self,side1):  #function

        return side1*side1;  

class Derived(arearect1,areasq2):  #derivedclass

    def Tri(self,x,y):  #function

        return (x**0.5)*y

d = Derived()  

print(d.Rect(50,30))  

print(d.Sq(5))  

print(d.Tri(5,10))