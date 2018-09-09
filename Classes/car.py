class Car():
    """A simple attempt to represent a car"""

    def __init__(self,make, model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """A statement showing a car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back.
        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_car = Car('audi','a4','2018')


print(my_car.get_descriptive_name())

my_car.update_odometer(23)
my_car.read_odometer()

my_car.increment_odometer(50)
my_car.read_odometer()

