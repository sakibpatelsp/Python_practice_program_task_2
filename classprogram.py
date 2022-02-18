#write a program to demonstrate parametarized constructor
class Person: #class
  def __init__(self, name, age): #constructor
    self.name = name
    self.age = age

sp = Person("sakib", 21)#object

print(sp.name)
print(sp.age)