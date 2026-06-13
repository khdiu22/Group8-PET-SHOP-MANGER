

from classes_1 import *
from classes_2 import *

def show_pets(shop):

    if len(shop.available_pets) == 0:
        print("No available pets.")
    else:
        for pet in shop.available_pets:
            pet.describe()

def confirm_sale():
    answer = input("Confirm sale? yes/no: ")
    if answer.lower() == "yes":
        return True
    else:
        return False
def main ():
    shop = PetShop()

    shop.add_pet(Dog("Lucky", "Dog", 2, 1200))
    shop.add_pet(Cat("Luna", "Cat", 1, 800))
    shop.add_pet(Bird("Rio", "Bird", 1, 300))

    shop.register_customer(Customer("Sara", "C-1"))
    shop.register_customer(Customer("Omar", "C-2"))
    shop.register_customer(Customer("Fatima", "C-3"))
    shop.register_customer(Customer("Khalid", "C-4"))
    shop.register_customer(Customer("Ahmed", "C-5"))
    shop.register_customer(Customer("Reem", "C-6"))

    while True:

        print("""
    ====== PET SHOP MANAGER ======
    1 - Add new pet
    2 - Register customer
    3 - Sell pet
    4 - Make pet speak
    5 - Show available pets
    6 - Shop stats
    7 - Filter pets by type
    8 - Exit
    """)

        choice = input("Choose: ")

        match choice:
            case "1":

                name = input("Name: ")
                species = input("Species Dog/Cat/Bird: ")

                try:
                    age = int(input("Age: "))
                    price = float(input("Price: "))

                except ValueError:
                    print("Age and price must be numbers.")
                    continue

                match species:
                    case "Dog":
                        pet = Dog(name, "Dog", age, price)

                    case "Cat":
                        pet = Cat(name, "Cat", age, price)

                    case "Bird":
                        pet = Bird(name, "Bird", age, price)

                    case _:
                        print("Unknown species.")
                        continue

                shop.add_pet(pet)

            case "2":

                name = input("Customer name: ")
                customer_id = input("Customer ID: ")

                customer = Customer(name, customer_id)

                shop.register_customer(customer)

            case "3":

                customer_id = input("Customer ID: ")
                pet_name = input("Pet name: ")

                if confirm_sale():
                    shop.sell_pet(customer_id, pet_name)
                else:
                    print("Sale cancelled.")

            case "4":

                pet_name = input("Pet name: ")

                pet = shop.find_pet(pet_name)

                if pet is None:
                    print("Pet not found.")
                else:
                    print(f"{pet.get_name()} says: {pet.make_sound()}")

            case "5":

                show_pets(shop)

            case "6":

                total_revenue = sum(pet.get_price() for pet in shop.sold_pets)

                print(f"Available pets: {len(shop.available_pets)}")
                print(f"Pets sold: {len(shop.sold_pets)}")
                print(f"Total revenue: {total_revenue} SAR")
                print(f"Species we sell: {shop.species_available}")

            case "7":

                species = input("Enter species Dog/Cat/Bird: ")

                shop.filter_by_type(species)

            case "8":

                print("Goodbye!")
                break

            case _:

                print("Invalid choice.")
        
main ()