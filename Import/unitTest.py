"""
This is the solution for the Homework #10: Importing

"""
import unittest
import xmlrunner


class Vehicle:
    def __init__(self, make, model, year, weight):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0

    # setters
    def setMake(self, make):
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
        return (" Make : {0} \n Model : {1} \n Year : {2} \n Weight : {3} \n NeedsMaintenance : {4} \n TripsSinceMaintenance : {5} \n".format(self.Make, self.Model, self.Year, self.Weight, self.NeedsMaintenance, self.TripsSinceMaintenance))


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


class CarsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n Tests related to Class Cars \n")

    def setUp(self):
        self.Polo = Cars("Volkswagen", "Polo", 2018, 1200)

    @unittest.skip("Skip Test")
    def test_nothing(self):
        self.fail("Test should not be executed.")

    def test_Initialize(self):
        self.assertEqual(self.Polo.Model, "Polo")
        self.assertEqual(self.Polo.Make, "Volkswagen")
        self.assertEqual(self.Polo.Year, 2018)
        self.assertEqual(self.Polo.Weight, 1200)

    def test_Drive(self):
        self.Polo.Drive()
        self.assertTrue(self.Polo.IsDriving)
        self.assertEqual(self.Polo.TripsSinceMaintenance, 0, "Trips Since Maintenance not correctly initialized.")

    def test_Stop(self):
        self.Polo.Drive()
        self.assertTrue(self.Polo.IsDriving)
        self.assertEqual(self.Polo.TripsSinceMaintenance, 0, "Trips Since Maintenance is not correctly initialized.")
        self.Polo.Stop()
        self.assertFalse(self.Polo.IsDriving)
        self.assertEqual(self.Polo.TripsSinceMaintenance, 1, "Trips Since Maintenance is not set correctly.")

    def test_NeedsMaintenance(self):
        for trip in range(50):
            self.Polo.Drive()
            self.Polo.Stop()
        self.assertFalse(self.Polo.NeedsMaintenance)

        for trip in range(51):
            self.Polo.Drive()
            self.Polo.Stop()
        self.assertTrue(self.Polo.NeedsMaintenance)

    def test_Repair(self):
        self.assertEqual(self.Polo.TripsSinceMaintenance, 0)
        self.assertFalse(self.Polo.NeedsMaintenance)

        for trip in range(101):
            self.Polo.Drive()
            self.Polo.Stop()

        self.assertEqual(self.Polo.TripsSinceMaintenance, 101)
        self.Polo.Repair()
        self.assertEqual(self.Polo.TripsSinceMaintenance, 0)
        self.assertFalse(self.Polo.NeedsMaintenance)


class PlanesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n Tests related to Class Planes \n")

    def setUp(self):
        self.Boeing = Planes("Boeing", "Dreamliner 787", 2018, 12000)

    def test_Flying(self):
        self.assertTrue(self.Boeing.Flying())
        self.assertTrue(self.Boeing.IsFlying)

    def test_Landing(self):
        self.assertTrue(self.Boeing.Flying())
        self.Boeing.Landing()
        self.assertFalse(self.Boeing.IsFlying)
        self.assertEqual(self.Boeing.TripsSinceMaintenance, 1)
        self.assertFalse(self.Boeing.NeedsMaintenance)

    def test_NeedsMaintainence(self):
        for trip in range(101):
            self.assertTrue(self.Boeing.Flying())
            self.Boeing.Landing()

        self.assertFalse(self.Boeing.Flying())
        self.assertTrue(self.Boeing.NeedsMaintenance)


def carsTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(CarsTest('test_Initialize'))
    suite.addTest(CarsTest('test_Drive'))
    suite.addTest(CarsTest('test_Stop'))
    suite.addTest(CarsTest('test_NeedsMaintenance'))
    suite.addTest(CarsTest('test_Repair'))
    suite.addTest(CarsTest('test_nothing'))
    return suite


def planesTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(PlanesTest('test_Flying'))
    suite.addTest(PlanesTest('test_Landing'))
    suite.addTest(PlanesTest('test_NeedsMaintainence'))
    return suite

if __name__ == "__main__":
    # unittest.main()
    # runner = unittest.TextTestRunner()
    with open('test-reports\carsTestSuite.xml', 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output)
        runner.run(carsTestSuite())

    with open('test-reports\planesTestSuite.xml', 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output)
        runner.run(planesTestSuite())
