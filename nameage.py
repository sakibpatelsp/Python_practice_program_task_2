'''Write a object oriented program to check class is subclass or not'''
class myAge: # base class

  age = 21

class myObj(myAge): #derived class

  name = 'Sakib Patel'

  age = myAge

x = issubclass(myObj, myAge) #object
print(x)