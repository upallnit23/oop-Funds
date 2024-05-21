#Task 2:Event Management System Enhancement

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date        

class Eventmods:
    def __init__(self):
        self.names = []

    def add_participant(self, name):
        self.names.append(name)    
        
    def get_participant_count(name):
        pass

eventmods = Eventmods()

name = input("Enter name of party: ")
date = input("Enter date of party: ")
eventmods.add_participant(Event(name, date))
print(name, date)
#eventmods.get_participant_count(name)


