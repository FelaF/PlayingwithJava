class Car:
    def __init__(self, name, make, model, year=int):
        self.name = name
        self.make = make
        self.model = model
        self.year = year

    def get_name(self):
        return self.name
    
    def __repr__(self):
        return f'{self.make} {self.model}'
    
"""Testing the fragility of my github fork"""

            

class Garage:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.contains = []

    def add_car(self, Car):
        if len(self.contains) < self.size: 
            self.contains.append(Car)
            return True
        else:
            return (f"It doesn't look like this car will
            fit because the garage size is {self.size}")
        return False

    def get_list_of_Cars(self):
        Carslist = []
        for car in self.contains:
            Carslist += Car.get_name()
            return Carslist
            


C1 = Car("Jim's", "Honda", "Civic", 2002)
C2 = Car("Tammy's", "Buggati", "Veyron", 2000)
C3 = Car("Aubrey's", "Toyota", "Camry", 2010)
C4 = Car("James\'", "Audi", "Q8", 2023)
C5 = Car("Ajani's", "Ford", "F150", 2020)

Mygarage = Garage("AJ", 4)
Mygarage.add_car(C1)
Mygarage.add_car(C5)
Mygarage.add_car(C2)
Mygarage.add_car(C3)

print(Mygarage.contains)


