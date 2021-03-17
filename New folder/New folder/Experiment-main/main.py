import datetime
start = datetime.datetime.now()
class Car:
    def __init__ (self,model,speed,tank_capacity,fuel_usage):
        self.model = model
        self.speed = speed
        self.tank_capacity = tank_capacity
        self.fuel_usage = fuel_usage

    def max_distance(self):
        return(self.tank_capacity * 100/self.fuel_usage)
    def max_duration(self):
        return(self.max_distance() / self.speed)#hour unit
    def is_better_than(self, other_car):
        if self.max_distance() > other_car.max_distance() and self.max_duration() > other_car.max_duration():
            return "yes"
        elif self.max_distance() < other_car.max_distance() and self.max_duration() < other_car.max_duration():
            return "no"
        else:
            return "maybe"

    def compare_cars(self, other_company):
        low = 0
        high= 0
        for a in other_company.cars:
            if self.is_better_than(a) == "yes":
                low += 1
                high += 1
            elif self.is_better_than(a) == "no":
                high += 1
        return (f"Our car, {self.model} is better than {low} out of {high} of all the cars in {other_company.name} company.")

class Company():
    def __init__(self, name, cars):
        self.name = name
        self.cars = cars

car1 = Car("Model S", 50, 37, 8.5)  
car2 = Car("Model 3", 45, 40, 10.2)
car3 = Car("Model 2", 55, 46, 7.9)
car4 = Car("Rock", 50, 45, 9.4)
car5 = Car("Mold", 52, 51, 23)
car6 = Car("Polder", 31, 52, 42)
car7 = Car("Willdon", 24, 61, 57)
car8 = Car("Smilt", 25, 61, 41)
car9 = Car("Polix", 56, 23, 51)
cara = Car("Loux", 79, 50, 54)

company2 = Company("Pasta de lamma", [car1, car2, car3, car4, car5, car6, car7, car8, car9, cara])

print(car4.is_better_than(car1)) # Prints "yes"
print(car2.is_better_than(car3)) # Prints "no"
print(car1.is_better_than(car2)) # Prints "maybe"

print(car4.compare_cars(company2)) # Prints "Our car, Rock is better than 2 out of 3 of all the cars in their company."
finish = datetime.datetime.now()
print ("my code :",finish-start)

