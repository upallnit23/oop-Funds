#City Infrastructure Management System
#Task 1:Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

v1 = Vehicle(615732, "Audi", "John Deere")
#print(f"{v1.reg_num}" is the vehicle registration number.)
print(f"{v1.owner} is the name of the owner.")

#new_owner = "Ben Tonka"
print(v1.update_owner("Ben Tonka"))
print(f"{v1.type} is the vehicle type, and {v1.owner} is the new owner.")




    



