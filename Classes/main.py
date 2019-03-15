"""
This is the solution for the Homework #9: Classes

"""


class Vehicle(object):
    def __init__(self, make, model, year, weight):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0

    # setters
    @property
    def Make(self):
        return self.Make

    @Make.setter
    def Make(self, make):
        self.Make = make

    def setModel(self, model):
        self.Model = model

    def setYear(self, year):
        self.Year = year

    def setWeight(self, weight):
        self.Weight = weight

    def ManageMaintainence(self):
        if(self.TripsSinceMaintenance > 100):
            self.NeedsMaintenance = True

    def Repair(self):
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0

    def __str__(self):
        return f"Make : {self.Make} \n Model : {self.Model} \n Year : {self.Year} \n Weight : {self.Weight} \n NeedsMaintenance : {self.NeedsMaintenance} \n TripsSinceMaintenance : {self.TripsSinceMaintenance} \n"


class Cars (Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.IsDriving = False

    def Drive(self):
        self.IsDriving = True

    def ManageTrips(self):
        if(self.IsDriving):
            self.TripsSinceMaintenance += 1

    def Stop(self):
        self.ManageTrips()
        self.IsDriving = False
        self.ManageMaintainence()


class Planes(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.IsFlying = False

    def ManageTrips(self):
        if(self.IsFlying):
            self.TripsSinceMaintenance += 1

    def Flying(self):
        if(self.NeedsMaintenance):
            self.IsFlying = False
            print("{0} {1} can't fly until it's repaired.".format(self.Make, self.Model))
        else:
            self.IsFlying = True
        return self.IsFlying

    def Landing(self):
        self.ManageTrips()
        self.IsFlying = False
        self.ManageMaintainence()

Polo = Cars("Volkswagen", "Polo", 2018, 1200)
Punto = Cars("Fiat", "Punto", 2015, 1159)
Audi = Cars("Audi", "A4", 2016, 1500)
CarLists = [Polo, Punto, Audi]

for trip in range(120):
    Punto.Drive()
    if(trip % 2 == 0):
        Polo.Drive()
    if(trip % 3 == 0):
        Audi.Drive()
    for car in CarLists:
        car.Stop()

for car in CarLists:
    print(car)

Boeing = Planes("Boeing", "Dreamliner 787", 2018, 12000)
Airbus = Planes("Airbus", "A380", 2017, 20000)
PlaneLists = [Boeing, Airbus]

for trip in range(120):
    Boeing.Flying()
    if(trip % 2 == 0):
        Airbus.Flying()
    for plane in PlaneLists:
        plane.Landing()

for plane in PlaneLists:
    print(plane)