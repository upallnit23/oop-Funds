import os

# Python City Planning Simulator
#Task 1:File Handling for Building Records

import fhbr

buildings = {}

def save_details():
    with open("randtext.txt", "w") as file:
        for building in buildings.values():
            file.write(f"{self.name}, {self.floor}")

def load_details():
    if os.path.exists("randtext.txt"):
        with open("randtext.txt", "r") as file:
            for line in file:
                name, floors = line.strip().split(",")
                floors = Building(name, floors)
                floors[name] = floors
            





 


