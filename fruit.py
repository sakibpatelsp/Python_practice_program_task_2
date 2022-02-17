

class fruit(): #class
     
    def __init__(self, fruitname, color): #constructor
        self.fruitname = fruitname
        self.color = color
         
    def show(self): #function
        print("fruitname is", self.fruitname )
        print("color is", self.color )
Fruit = fruit("mango", "yellow")
Fruit.show()     #function call