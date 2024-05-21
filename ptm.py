class Bus:
    def __init__(self, bus_num, size, city, direction, route, fare):
        self.bus_num = bus_num
        self.size = size
        self.city = city
        self.direction = direction
        self.route = route
        self.fare = fare

    def travel_Outercity(self, bus_num = 1552, size = "long", city = "Calumet", route = "north", fare = 2.00):
        bus_num = input("Enter bus number: ")
        print(f"#{bus_num}, bus type {size} is traveling to {city}, via route {route}.")
        print(f"Total fare is ${fare}")

    def travel_Loop(self, bus_num = 1526, size = "short", city = "Loop", route = "east", fare = 1.00):
        bus_num = input("Enter bus number: ")
        print(f"#{bus_num}, bus type {size} is traveling to {city}, via route {route}.")
        print(f"Total fare is ${fare}")
    
    def travel_City(self, bus_num = 1555, size = "reg", city = "Chicago", route = "south", fare = 1.50):
        bus_num = input("Enter bus number: ")
        print(f"#{bus_num}, bus type {size} is traveling to {city}, via route {route}.")
        print(f"Total fare is ${fare}")

    def passenger_cap(self, size):
        if self.size == "short":
            pcap = 50
        elif self.size == "reg":
            pcap = 60
        elif self.size == "long":
            pcap = 75
        else:
            pcap = 50
    
b1 = Bus(1, "short", "Chicago", "east", "west", 1.00)
print(f"#{b1.bus_num} from {b1.city} is traveling {b1.route}.")

b2 = Bus.travel_Loop(1)
print(b2)
