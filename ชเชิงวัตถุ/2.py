class Vehicle:
    licenCode = ''
    serialCode = ''
    def Aircondition(self):
        print('Aircondition on')
        print('wowww')

class Car(Vehicle):
    def Aircondition(self):
        print('Aircondition onnnnn')

car = Car()
car.Aircondition()
