class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print('Brand: ', self.brand)
        print('Year: ', self.year)


class Car(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def display_info(self):
        super().display_info()
        print('Color: ', self.color)


class Motorcycle(Vehicle):
    def __init__(self, brand, year, color, model):
        super().__init__(brand, year)
        self.model = model
        self.color = color

    def display_info(self):
        super().display_info()
        print('Model: ', self.model)
        print('Color: ', self.color)

car = Car("Gentra", 2023, "black")
motorcycle = Motorcycle("Honda", 2019, 'Blue' 'C454', 'AAA')

print("       Car Info:")
car.display_info()
print("     Motorcycle Info:")
motorcycle.display_info()
