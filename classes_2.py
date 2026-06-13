
class PetShop:

    def __init__(self):

        self.available_pets = [] #list
        self.sold_pets = [] 
        self.customers = {}
  
        self.species_available = set()

    def add_pet(self, pet):# 

        self.available_pets.append(pet) 
        # اضافه حيوانات جديده للمتجر  
        self.species_available.add(pet.species) 
        print("Pet added!")

    def register_customer(self, customer): # تسجيل  عميل جديد

        if customer.customer_id in self.customers:
           print("Customer already exists!")
        else:
            self.customers[customer.customer_id] = customer 
            print("Customer registered!")

    def find_pet(self, pet_name): 
        for pet in self.available_pets + self.sold_pets: # دمج القائمه  ويمر على كل الحيوانات
            if pet.get_name().lower() == pet_name.lower(): # الحصول على اسم الحيوان وتحويله لحروف صغيره
                return pet # يعيد كاين الحيوان بالكامل
        return None 

    def sell_pet(self, customer_id, pet_name):

        if customer_id not in self.customers: # التاكد من وجود العميل
            print("Customer not found!")
            return 

        pet = self.find_pet(pet_name) # استدعاد داله البحث سابقا 
        if pet is None:
            print("Pet not found!")
            return

        if pet.is_available == False: 
            print("Already sold!")
            return 

        customer = self.customers[customer_id] 
        pet.is_available = False 
        self.available_pets.remove(pet) 
        self.sold_pets.append(pet) 
        customer.pets_bought.append(pet)  
        print(
            f"{customer.get_name()} bought! " 
            f"{pet.get_name()} for {pet.get_price()} SAR." 
        )

    def filter_by_type(self, species): 
        found = False # متغير يستخدم  لمعرفه هل وجدنا نتائج ام لا
        for pet in self.available_pets:
            if pet.species.lower() == species.lower():
                found = True
                match pet.species:
                    case "Dog":
                        print("Dog available:")
                    case "Cat":
                        print("Cat available:")
                    case "Bird":
                        print("Bird available:")
                    case _:
                        print("Other pet:")
                pet.describe()
        if found == False:
            print("No pets found for this type.")
