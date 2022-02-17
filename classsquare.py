"""write a program to find area of square using class"""


class square: #class
    def __init__(self, s): #constructor
        self.side = s

    def area(self): #function
        return self.side**2
Newsquare = square(5) #object
print(Newsquare.area()) #function call