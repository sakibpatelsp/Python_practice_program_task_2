class Person: #class
  def __init__(self, name, age): #constructor
    self.name = name
    self.age = age

  def myfunc(n):
    print("Hello my name is " + n.name)
    print("Hello my age is " + n.age)

p1 = Person("Sakib", '21')
p1.myfunc() #function call