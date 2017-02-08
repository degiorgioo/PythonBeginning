from FirstClass.Classes import *

car1 = Car("Ferrari", 200)
battery1 = Battery(100)
electricCar1 = ElectricCar("BMW", 200, battery1)

electricCar1.battery.showlifetime()
