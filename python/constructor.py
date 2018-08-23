'''class Person:
    def __init__(self,name,course):
        self.name = name
        self.course = course
 
    def getName(self):
        return self.name
 
    def getCourse(self):
        return self.course
 
name=input("Enter the name : \t")
course= input("Enter the course : \t")
student = Person(name,course)
print(student.getName())
print(student.getCourse())'''

class Veichle:
    TAX = 0.13
    ADDITIONAL_MARGIN = 10000
    def __init__(self,price,manufacture):
        self.price = price
        self.manufacture = manufacture
 
    def getSellingPrice(self):
        return self.price+self.price*self.TAX + self.ADDITIONAL_MARGIN
 
    def getManufacture(self):
        return self.manufacture
 
 
pulsar = Veichle(250000, "Bajaz")
print("Pulsar price = {} and manufacture is {}".format(pulsar.getSellingPrice(),pulsar.getManufacture()))
