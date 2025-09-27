# task 1
class User:
    def __init__(self, first_name, last_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def __str__(self):
        return f"User({self.__first_name} {self.__last_name}, Email: {self.__email})"

user = User("Name", "Surname", "example@gmail.com", "password")
print(user)
user.set_first_name("newEmail@gmail.com")
user.set_password("newPassword")
print(user)


# task 2
import math

class Shape:
    _type = "Shape"
      
    def __init__(self, area = None, sizes = None):
        self._area = area
        self._sizes = sizes if sizes else {}
    
    def get_type(self):
        return self._type
    
    def set_type(self, type):
        self._type = type

    def get_area(self):
        if(self._area):
            return self._area
        raise NotImplementedError("This method should be overridden in derived classes")

    def get_sizes(self):
        return self._sizes
    
    def set_sizes(self, sizes):
        self._sizes = sizes

    def __str__(self):
        return f'{self._type} with sizes: {self._sizes} and area: {self.get_area()}'

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(sizes={"radius": radius})
        self._type = "Circle"

    def set_sizes(self, sizes):
        self._sizes = {"radius": sizes}

    def get_area(self):
        return math.pi * self._sizes["radius"] ** 2

# circle = Circle(5)
# print(circle)
# circle.set_sizes(8)
# print(circle)


# task 3
class Vehicle:
    _type = "Vehicle"

    def __init__(self, price, wheels_amount, max_speed, passangers_amount):
        self._price = price
        self._max_speed = max_speed
        self._wheels_amount = wheels_amount
        self._passangers_amount = passangers_amount
    
    def get_type(self):
        return self._type

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price
    
    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed
    
    def set_passangers_amount(self, passangers_amount):
        self.passangers_amount = passangers_amount

    def get_passangers_amount(self):
        return self._passangers_amount
    
    def get_wheels_amount(self):
        return self._wheels_amount

    def action(self) -> None:
        print(f"{self._type} goes wroom wroom on {self._max_speed} km/h and {self._passangers_amount} people")
 
    def crashed(self) -> None:
        print(f"{self._type} was crashed. Everybody is alive. {self._wheels_amount} wheels are all apart now. {self._price} $ was just destroyed")

    def can_be_bought(self, money) -> bool:
        return money >= self._price
    
    def can_transport_amount(self, amount) -> bool:
        return amount <= self._passangers_amount

class Car(Vehicle):
    _type = "Car"

    def __init__(self, price, max_speed, passangers_amount, has_spare_wheel):
        super().__init__(price, 4, max_speed, passangers_amount)
        self._has_spare_wheel = has_spare_wheel

    def set_spare_wheel(self, has_spare_wheel):
        self._has_spare_wheel = has_spare_wheel

    def get_spare_wheel(self):
        return self._has_spare_wheel
    
    def can_borrow_wheel(self) -> bool:
        return self._has_spare_wheel
    
class Motorcycle(Vehicle):
    _type = "Motorcycle"

    def __init__(self, price, max_speed, passangers_amount, is_epic):
        super().__init__(price, 2, max_speed, passangers_amount)
        self._is_epic = is_epic
        
    def people_reaction(self) -> None:
        reaction = "Hell Yeah, it is epic!!" if self._is_epic else f"Not that epic, costs only {self._price}"  
        print(reaction)

class Bicycle(Vehicle):
    _type = "Bicycle"

    def __init__(self, price, max_speed, has_bag):
        super().__init__(price, 2, max_speed, 1)
        self._has_bag = has_bag
        
    def is_usefull(self) -> bool:
        return self._has_bag
    
# car = Car(5000, 150, 4, True)
# car.action()
# print(f"Can borrow spare wheel? - {car.can_borrow_wheel()}")
# car.set_spare_wheel(False)
# print(f"Can borrow spare wheel? - {car.can_borrow_wheel()}")
# print(f"Can be bought on 4000 $ - {car.can_be_bought(4000)}")

# motorcycle = Motorcycle(4000, 120, 2, True)
# motorcycle.action()
# motorcycle.people_reaction()
# motorcycle.crashed()

# bicycle = Bicycle(250, 20, False)
# bicycle.action()
# print(f"Is it useful? - {bicycle.is_usefull()}")
# print(f"{bicycle.get_type()} can hold only "
#       f"{bicycle.get_passangers_amount()} "
#       "people and has only "
#       f"{bicycle.get_wheels_amount()} wheels")

# task 4
class MedicalStaff:
    _type = "MedicalStaff"

    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def register_patient(self, patient_name):
        print(f"{self.name} is registering patient {patient_name}.")

    def provide_medical_care(self, patient_name):
        print(f"{self.name} is providing medical care to patient {patient_name}.")

class Doctor(MedicalStaff):
    _type = "Doctor"

    def provide_medical_care(self, patient_name):
        print(f"{self._type} {self.name} is providing medical care to patient {patient_name}.")
        self.prescribe_meds()

    def prescribe_meds(self):
        print(f"{self._type} {self.name} is prescribing treatment and more observation tasks.")

class Nurse(MedicalStaff):
    _type = "Nurse"

    def provide_medical_care(self, patient_name):
        print(f"{self._type} {self.name} is providing medical care to patient {patient_name}.")
        self.perform_meds()

    def perform_meds(self):
        print(f"{self._type} {self.name} is performing order.")

class Administrator(MedicalStaff):
    _type = "Administrator"

    def register_patient(self, patient_name):
        print(f"{self._type} {self.name} is registering patient {patient_name}.")

    def organize_appointment(self, patient_name, doctor: Doctor, nurse: Nurse):
        print(f"{self._type} {self.name} is organizing an appointment for the {patient_name}"
               f"with {doctor.name}-{doctor.id_number} and {nurse.name}-{nurse.id_number}.")
        doctor.provide_medical_care(patient_name)
        nurse.perform_meds()


# doctor = Doctor("Doctor1", 45, "123")
# nurse = Nurse("Nurse1", 30, "456")
# administrator = Administrator("Administrator1", 35, "789")

# doctor.register_patient("Guy1")
# doctor.provide_medical_care("Guy1")

# nurse.register_patient("Guy2")
# nurse.provide_medical_care("Guy2")

# administrator.register_patient("Guy3")
# administrator.organize_appointment("Guy3", doctor, nurse)


# task 5
class MathAction:
    def calculate(self, x, y) -> float:
        raise NotImplementedError("This method should be overridden in derived classes")

class Addition(MathAction):
    def calculate(self, x, y) -> float:
        return x + y

class Subtraction(MathAction):
    def calculate(self, x, y) -> float:
        return x - y

class Multiplication(MathAction):
    def calculate(self, x, y) -> float:
        return x * y

class Division(MathAction):
    def calculate(self, x, y) -> float:
        if y == 0:
            raise ZeroDivisionError("Error: Division by zero")
        return x / y

# add = Addition()
# subtract = Subtraction()
# multiply = Multiplication()
# divide = Division()

# try:
#     print("Addition: 1, 2 = ", add.calculate(1, 2))
#     print("Subtraction: 3, 4 = ", subtract.calculate(3, 4))
#     print("Multiplication: 5, 6 =", multiply.calculate(5, 6))
#     print("Division: 7, 8 = ", divide.calculate(7, 8))
#     print("Division: 9, 0 = ", divide.calculate(9, 0))
# except ZeroDivisionError as e:
#     print(e)


# task 6
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def display(self) -> None:
        pass

    def choose(self, value) -> bool:
        pass


class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.__warranty = warranty

    def display(self) -> None:
        print(f"Name: {self._name}, Price: {self._price} $, Warranty: {self.__warranty} m")

    def choose(self, warranty_required) -> bool:
        if not warranty_required:
            return True
        return self.__warranty > 0

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.__size = size

    def display(self) -> None:
        print(f"Name: {self._name}, Price: {self._price} $, Size: {self.__size} EU")

    def choose(self, size) -> bool:
        return size <= self.__size

class Groceries(Product):
    def __init__(self, name, price, expiry_date):
        super().__init__(name, price)
        self.__expiry_date = expiry_date

    def display(self) -> None:
        print(f"Name: {self._name}, Price: {self._price} $, Expiry Date: {self.__expiry_date} d")

    def choose(self, expiry_date) -> bool:
        return expiry_date <= self.__expiry_date


# electronics = Electronics("Laptop", 1200, 12)
# clothing = Clothing("T-shirt", 25, 42)
# groceries = Groceries("Milk", 3, 5)

# products = [electronics, clothing, groceries]
# filters = [False, 44, 3]

# for i in range(len(products)):
#     products[i].display()
#     print(f"Could be chosed by filter {filters[i]} - {products[i].choose(filters[i])}")
    

# task 7
class Employee:
    def __init__(self, name, position=None, salary=0):
        self.name = name
        self.position = position
        self.salary = salary

    def raise_salary(self, percent):
        self.salary += round(self.salary * percent, 2)

    def __str__(self):
        return (f"Name: {self.name}\nPosition: {self.position}\nSalary: {self.salary:.2f} grn")

class Manager(Employee):
    def raise_salary(self, percent, bonus_percent):
        self.salary += round(self.salary * (percent + bonus_percent), 2)


# manager = Manager("Manager1", "Manager", 20000.00)
# manager.raise_salary(0.3, 0.25)
# print(manager)
