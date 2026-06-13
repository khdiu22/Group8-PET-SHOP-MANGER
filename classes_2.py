
class PetShop:

    def __init__(self):
#  اتريبيوت او خصائص
        self.available_pets = [] #list
        self.sold_pets = [] # list
        self.customers = {} #  الهدق الوصول السريع للايدي دكشنري ليش لانه اسهل واسرع من اني ادور رقم باللست كامله 
        self.species_available = set()

    def add_pet(self, pet):# 

        self.available_pets.append(pet) # هذا لست لذاك اضفنا append للاضافه  هنا راح تضاف القيم الي حهزناها فالكزنستركتر الي فوق
        # اضافه حيوانات جديده للمتجر  
        self.species_available.add(pet.species) # هذا اللمر لايتكرر هو  set
        print("Pet added!")

    def register_customer(self, customer): # تسجيل  عميل جديد

        if customer.customer_id in self.customers: # يفحص هل   العميل مسجل مسبقا او لا
            print("Customer already exists!")
        else:
            self.customers[customer.customer_id] = customer # دكشنري  الي داخل القوس  مفتاح  الي داخل الاقواس تعني الوصول الى العنصر داخل الدكشنري
            print("Customer registered!")

    def find_pet(self, pet_name): # البحث عن الحيوان بالاسم
        for pet in self.available_pets + self.sold_pets: # دمج قائمه  ويمر على كل الحيوانات
            if pet.get_name().lower() == pet_name.lower(): # الحصول على اسم الحيوان وتحويله لحروف صغيره
                return pet # يعيد كاين الحيوان بالكامل
        return None # اذا لم يجده 

    def sell_pet(self, customer_id, pet_name):# التاكد من وجود العميل والتاكد من وجود الحيوانو التاكد ان الحيوان غير مباع و نقل الحيوان المتاح الى المباعو اضافه الى قائمه المشتريات للعميل

        if customer_id not in self.customers: # التاكد من وجود العميل
            print("Customer not found!")
            return # يوقف الداله اذا لم يجده 

        pet = self.find_pet(pet_name) # استدعاد داله البحث سابقا 
        if pet is None:
            print("Pet not found!")
            return

        if pet.is_available == False: # اذا كان الحيوان مباع سابقا  اليساوي هنا يعني مقارنه 
            print("Already sold!")
            return 

        customer = self.customers[customer_id] # ياخذ العميل من الدكشنري ويحفظه في متغير اسمه كستمر
        pet.is_available = False # تغير حاله البيع 
        self.available_pets.remove(pet) # حذف العنصر من القائمه 
        self.sold_pets.append(pet) # وراح ينضاف هنا 
        customer.pets_bought.append(pet)  #  نضيف الحيوام الى قائمه مشتريات العميل  
        print(
            f"{customer.get_name()} bought! " # ترجع لي اسم العميل 
            f"{pet.get_name()} for {pet.get_price()} SAR." #ترجع اسم الحيوان ترجع نوعه
        )

    def filter_by_type(self, species): # عرض الحيوانات المتاحه  حسب النوع 
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
