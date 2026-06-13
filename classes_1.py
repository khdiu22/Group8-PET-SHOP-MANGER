

class Pet:

    def __init__(self, name, species, age, price):
        self._name = name
        self.species = species
        self.age = age
        self._price = price
        self.is_available = True

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def make_sound(self):
        return "..."

    def describe(self):
        print(
            f"Name: {self.get_name()} | "
            f"Species: {self.species} | "
            f"Age: {self.age} | "
            f"Sound: {self.make_sound()} | "
            f"Price: {self.get_price()} SAR"
        )

    def apply_discount(self, pct):
        self._price = self._price * (1 - pct / 100)

    def pet_info(self):
        return (self.get_name(), self.species, self.age, self.get_price())



class Dog(Pet):
    def make_sound(self):
        return "Woof!"

class Cat(Pet):
    def make_sound(self):
        return "Meow!"

class Bird(Pet):
    def make_sound(self):
        return "Tweet!"


class Customer:

    def __init__(self, name, customer_id):

        self._name = name
        self.customer_id = customer_id
        self.pets_bought = []

    def get_name(self):
        return self._name