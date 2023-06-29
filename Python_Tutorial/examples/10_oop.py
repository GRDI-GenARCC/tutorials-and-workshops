class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2021)


print(car1.make)  # Output: Toyota
print(car2.year)  # Output: 2021

car1.drive()  # Output: The Toyota Camry is driving.
car2.drive()  # Output: The Honda Accord is driving.
