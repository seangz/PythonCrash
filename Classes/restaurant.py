class Restaurant():
    """A class for restaurants"""

    def __init__(self, restaurant_name, cuisine_type):

        """Initialize name and type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.capitalize() + " is really good. They have " + self.cuisine_type.title() + " food there.")

    def restaurant_open(self):
        print(self.restaurant_name.capitalize() + " is open!")

    def served(self):
        print('They have served ' + str(self.number_served) + ' guests so far')

    def set_number_served(self, guests):
        self.number_served = guests

    def update_guests(self, update):
        self.number_served += update



sean = Restaurant('sean','sri lankan')

Restaurant.describe_restaurant(sean)
sean.served()

sean.set_number_served(15)
sean.served()

sean.update_guests(14)
sean.served()

