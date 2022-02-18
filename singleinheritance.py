class proverb:  
    def apple(self):  
        print("an appple a day keeps doctor away")  
#child class Dog inherits the base class Animal  
class proverb1(proverb):  
    def success(self):  
        print("Hard work is  a symbol of success")  
d = proverb1()  
d.apple()  
d.success()  