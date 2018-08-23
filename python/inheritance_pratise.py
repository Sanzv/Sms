# class Viechle is created
# lets assume this is the base class often called parent 
# In base class the most generic methods and variables are kept which is more like similiar in all child class
class Veichle:
    TAX = 0.13
    ADDITIONAL_MARGIN = 10000
    discount=0.10
    def __init__(self,price,manufacture):
        self.price = price
        self.manufacture = manufacture
 
    def getSellingPrice(self):
        return self.price+self.price*self.TAX + self.ADDITIONAL_MARGIN
 
    def getManufacture(self):
        return self.manufacture

    def allowDiscount(self):
        self.price=self.price - self.price*self.discount
        print("Price after Discount = {}".format(self.price))


    def getPrice(self):
        return self.price
 
# This class is inherited from the Veichle
# In the bracket the class name given from which it is inherited
 
class MotorBike(Veichle):
    def __init__(self, manufacture):
        Veichle.__init__(self, 250000, manufacture)
 
    def getNumberOfWheels(self):
        return 2
 
    def getRoadtax(self):
        return 4000
 
 
pulsar = MotorBike("Bajaj")
# Here pulsar is the object of the Motorbike but it has the method of the Veichle class aswell
# This is what inheritance features
print("Selling price = {} ".format(pulsar.getSellingPrice()))
pulsar.allowDiscount()
print("manufacturer = {}".format(pulsar.getManufacture()))
print("Number of wheels = {}".format(pulsar.getNumberOfWheels()))
print("Road Tax = {}".format(pulsar.getRoadtax()))