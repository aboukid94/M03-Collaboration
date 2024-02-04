# super class
class Vehicle:
    
    def __init__(self, vehicle_type):
        
        self.vehicle_type = vehicle_type


# lower class
class Automobile(Vehicle):
    
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        
        # calls super class constructor
        Vehicle.__init__(self, vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # returns data in required format
    def __str__(self):
        
        return "Vehicle type: " + self.vehicle_type + "\nYear: " + self.year + "\nMake: " + self.make + "\nModel: " + self.model + "\nNumber of doors: " + self.doors + "\nType of roof: " + self.roof


if __name__ == "__main__":
    
    # asks for input of car year, make, model, number of doors, and roof type.
    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")
    doors = input("Enter number of doors: ")
    roof = input("Enter type of roof: ")
    
    # creates object of vehicle type as a car
    carObj = Automobile("car", year, make, model, doors, roof)
    
    # prints details
    print()
    print()
    print()
    print()
    print("The information you entered is: ")
    print(carObj)
    
    