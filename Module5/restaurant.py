#ScarletPrescott
class Restaurant:
    """Simply attempt to model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is open!")

    def set_number_served(self, number_served):
        self.number_served += abs(number_served)

    def increment_number_served(self, additional_served):
        self.number_served += additional_served
