class Person:
    def __init__(self, firstname, lastname, age):
        """constructor"""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def introduceyourself(self):
        print("Hi, my name is " + self.firstname + " " + self.lastname + " and i am " + str(self.age) + " years old.")


class Car:
    def __init__(self, brandname, power):
        print("Car constructor")
        self.brandname = brandname
        self.power = power

    def describeyoureself(self):
        print(self.brandname + " " + str(self.power))


class ElectricCar(Car):
    def __init__(self, brandname, power, battery):
        super().__init__(brandname, power)
        print("ElectricCar constructor")
        self.battery = battery

    def batterylifetime(self):
        print(self.battery.capacity)


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def showlifetime(self):
        print(self.capacity)
