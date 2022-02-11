class Fruit:
    
    def __init__(self):
        self.__maxprice = 90

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Fruit()
c.sell()

# change the price
c.__maxprice = 100
c.sell()

# using setter function
c.setMaxPrice(100)
c.sell()