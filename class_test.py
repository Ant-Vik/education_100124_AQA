


class Auto:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self, speed_increase):
        self.speed += speed_increase

    def brake(self, speed_increase):
        self.speed -= speed_increase

    def get_speed(self):
        return self.speed


class Car(Auto):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def honk(self):
        return "Beep"



class Motorcycle(Auto):
    def __init__(self, make, model, has_speedecar):
        super().__init__(make, model)
        self.has_speedecar = has_speedecar

    def wheelie(self):
        if not self.has_speedecar:
            return "Performing a wheelie"
        else:
            return "Cannot performing a wheelie"

my_motorcycle = Motorcycle("Harley", "SSS", True)
my_motorcycle.accelerate(190)
print("motorcycle wheelie", my_motorcycle.wheelie())



my_car = Car("Toyota", "Camry", 4)
my_car.accelerate(100)
print("Car honk", my_car.honk())
print("Car speer", my_car.get_speed())

