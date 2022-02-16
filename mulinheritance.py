'''Write a Program to demonstrate multiple inheritance'''

class Calculation1:  #baseclass

    def Sum(self,a,b):  #function

        return a+b;  

class Calculation2:  #baseclass

    def Multiplication(self,a,b):  #function

        return a*b;  

class Derived(Calculation1,Calculation2):  #derivedclass

    def Divide(self,a,b):  #function

        return a/b;  

d = Derived()  

print(d.Sum(50,300))  

print(d.Multiplication(30,25))  

print(d.Divide(625,25))