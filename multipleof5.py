''' Python program to check whether the given integer is a multiple of 5 '''
class Mul: #class
    def multiple(self): #function
        number = int(input("Enter an integer: "))
        if(number%5==0):
            print(number, "is a multile of 5")
        else:
            print(number, "is not a multiple of 5")
a=Mul() #object
a.multiple() #function call