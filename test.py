class Garage:
    vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)


class Vehicle:
    def __init__(self, age):
        self.age = age


class Car(Vehicle):
    def __init__(self, doors, age):
        super().__init__(age)
        self.doors = doors

class Bike(Vehicle):
    pass

garage = Garage()
newCar = Car(5, 5)
garage.add_vehicle(newCar)
newCar = Car(3, 2)
garage.add_vehicle(newCar)
newCar = Bike(3)
garage.add_vehicle(newCar)
print(garage.vehicles)

for vehicle in garage.vehicles:
    print(isinstance(vehicle, Vehicle))
    print(isinstance(vehicle, Car))
