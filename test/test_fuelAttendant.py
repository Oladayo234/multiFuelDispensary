from unittest import TestCase

from multi_fuel_dispensary.FuelAttendant import FuelAttendant
from multi_fuel_dispensary.Dispenser import Dispenser
from multi_fuel_dispensary.Fuel import Fuel


class TestFuelAttendant(TestCase):


    def setUp(self) -> None:
        self.dispenser = Dispenser()
        self.attendant = FuelAttendant("Oladayo Ajomole", self.dispenser)
        self.petrol = Fuel(50, "petrol", 65.50)
        self.diesel = Fuel(50, "diesel", 65.50)

    def test_that_the_attendant_can_sell_fuel_by_liter(self):
        self.attendant.add_fuel(self.petrol)
        transaction = self.dispenser.dispense_fuel_by_liter("petrol", 10.0)
        self.attendant.generate_receipt(transaction)

        self.assertEqual(self.petrol.get_quantity(), 40.0)
        self.assertEqual(transaction["liters"], 10)
        self.assertEqual(transaction["total"], 655.0)
        self.assertEqual(len(self.attendant.get_sales_records()), 1)

    def test_that_the_attendant_can_sell_fuel_by_amount(self):
        self.attendant.add_fuel(self.petrol)
        transaction = self.dispenser.dispense_fuel_by_amount("petrol", 655.0)
        self.attendant.generate_receipt(transaction)

        self.assertEqual(self.petrol.get_quantity(), 40.0)
        self.assertEqual(transaction["total"], 655.0)
        self.assertEqual(transaction["fuel_type"], "petrol")
        self.assertEqual(len(self.attendant.get_sales_records()), 1)

    def test_that_the_attendant_can_restock_fuel(self):
        self.attendant.add_fuel(self.petrol)
        self.attendant.restock_fuel(self.petrol, 50)
        self.assertEqual(self.petrol.get_quantity(), 100.0)

    def test_that_attendant_can_have_multiple_fuel_sales(self):
        self.attendant.add_fuel(self.petrol)
        self.attendant.add_fuel(self.diesel)
        transaction1 = self.dispenser.dispense_fuel_by_liter("petrol", 10.0)
        transaction2 = self.dispenser.dispense_fuel_by_liter("diesel", 20.0)

        self.attendant.generate_receipt(transaction1)
        self.attendant.generate_receipt(transaction2)
        self.assertEqual(self.petrol.get_quantity(), 40.0)
        self.assertEqual(self.diesel.get_quantity(), 30.0)
        self.assertEqual(len(self.attendant.get_sales_records()), 2)