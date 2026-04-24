class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model= model
        self.year= int(year)
        
    def __str__(self):
        return str(self.vid)+"," + str(self.model)+"," +str(self.year)
    
    def __eq__(self, other):
        return self.vid== other.vid
        
    def is_new(self,n):
        return self.year >= (2026-n)
        
        
        
        
class Car(Vehicle):
    def __init__(self,vid, model, year, fuel_type, doors):
         super().__init__(vid, model, year)
         self.fuel_type= fuel_type
         self.doors= int(doors)
         
    def __str__(self):
        return "[Car] VID: " + str(self.vid)+" | " + str(self.model)+" (" +str(self.year)+") | Fuel: " +str(self.fuel_type)+ " | " +str(self.doors)+" Doors"
  
  
  
        
class Truck(Vehicle):
    def __init__(self,vid, model, year,max_load , axles):
         super().__init__(vid, model, year)
         self.max_load= int(max_load)
         self.axles= int(axles)
         
    def __str__(self):
        return "[Truck] VID: " + str(self.vid)+" | " + str(self.model)+" (" +str(self.year)+") | Load: " +str(self.max_load)+" kg | " +str(self.axles)+ " Axles"
        
        
        
class Motorcycle(Vehicle):
    def __init__(self,vid, model, year,engine_cc , v_type):
         super().__init__(vid, model, year)
         self.engine_cc= int(engine_cc)
         self.v_type= v_type
         
    def __str__(self):
        return "[Motorcycle] VID: "+ str(self.vid)+" | " + str(self.model)+" (" +str(self.year)+") | Eng: " +str(self.engine_cc)+"cc | Type: " +str(self.v_type)
        
    
        
    
def save_fleet_to_file(vehicles, filename):  
    
    file= open(filename, "w")
    
    for v in vehicles:
        if type(v)== Car:
            file.write("Car, " + v.vid +", " +v.model +", "+ str(v.year)+", " +v.fuel_type+", " + str(v.doors) +"\n")
            
        elif type(v)== Truck:
            
            file.write("Truck, " + v.vid +", " +v.model +", " +str(v.year)+", " +str(v.max_load)+", " + str(v.axles) +"\n")
            
        elif type(v)== Motorcycle:
            
            file.write("Motorcycle, " + v.vid +", " +v.model +", " +str(v.year)+", " +str(v.engine_cc)+", " + v.v_type +"\n")
            
    file.close()
            
            
            
def load_fleet_from_file(filename):
    
    vehicles= []
    
    file = open(filename, "r")
    lines= file.readlines()
    file.close()
    
    for line in lines:
        parts= line.strip().split(", ")
        v_type= parts[0]
        
        if v_type== "Car":
            car_obj= Car(parts[1],parts[2], parts[3], parts[4], parts[5])
            vehicles.append(car_obj)
            
        elif v_type== "Truck":
            truck_obj= Truck(parts[1],parts[2], parts[3], parts[4], parts[5])
            vehicles.append(truck_obj)
            
        elif v_type== "Motorcycle":
            motor_obj= Motorcycle(parts[1],parts[2], parts[3], parts[4], parts[5])
            vehicles.append(motor_obj)
        
    
    return vehicles
    

car1 = Car("V001", "Tesla Model 3" ,2023, "Electric", 4)
truck1 = Truck("T001", "Volvo FH16" ,2019, 25000, 6)
motor1 = Motorcycle("M001", "Yamaha R1 " ,2024, 998, "Sport")
car2 = Car("V002", "Toyota Corolla" ,2018, "Petrol", 4)
truck2 = Truck("T002", "Mercedes Actros" ,2021, 18000, 4)
motor2 = Motorcycle("M002", "Harley Davidson" ,2015, 1200, "Cruiser")


vehicles= [car1,truck1, motor1, car2,truck2, motor2]

save_fleet_to_file(vehicles, "fleet.txt")
print("Loading fleet data from 'fleet.txt'...")
loaded_vehicles = load_fleet_from_file("fleet.txt")
print(str(len(loaded_vehicles))+ " vehicles loaded successfully.")

print("\n--- All Vehicles ---")
for v in loaded_vehicles:
    print( v)

print("\n--- Recent Vehicles (Last 4 Years) ---")
for v in loaded_vehicles:
    if v.is_new(4):
        print(v)
        
print("\n--- Electric Cars Only ---")
for v in loaded_vehicles:
    if type(v)== Car and v.fuel_type== "Electric":
        print(v)
