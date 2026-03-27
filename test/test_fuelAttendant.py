import os
import unittest
from multi_fuel_dispensary.FuelAttendant import FuelAttendant
from multi_fuel_dispensary.Dispenser import Dispenser
from multi_fuel_dispensary.Fuel import Fuel

class TestFuelAttendant(unittest.TestCase):

    def setUp(self):
        self.dispenser = Dispenser()
        self.attendant = FuelAttendant(full_name="John Doe", dispenser=self.dispenser)
        self.petrol = Fuel(quantity=50.0, fuel_type="petrol", price_per_liter=65.50)
        self.diesel = Fuel(quantity=50.0, fuel_type="diesel", price_per_liter=74.50)

    def tearDown(self):
        if os.path.exists("fuel_store.json"):
            os.remove("fuel_store.json")
        if os.path.exists("transaction_history.txt"):
            os.remove("transaction_history.txt")

    def test_that_attendant_can_be_created_with_correct_inputs(self):
        self.assertEqual(self.attendant.get_full_name(), "John Doe")
        self.assertEqual(self.attendant.get_sales_records(), [])

    def test_that_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            FuelAttendant(full_name="", dispenser=self.dispenser)

    def test_that_non_string_name_raises_error(self):
        with self.assertRaises(TypeError):
            FuelAttendant(full_name=123, dispenser=self.dispenser)

    def test_that_name_is_stripped_of_whitespace(self):
        attendant = FuelAttendant(full_name="  John Doe  ", dispenser=self.dispenser)
        self.assertEqual(attendant.get_full_name(), "John Doe")

    def test_that_fuel_can_be_added(self):
        self.attendant.add_fuel(self.petrol)
        self.assertEqual(self.dispenser.get_fuel("petrol"), self.petrol)

    def test_that_add_fuel_raises_error_for_non_fuel_object(self):
        with self.assertRaises(TypeError):
            self.attendant.add_fuel("petrol")

    def test_that_fuel_can_be_retrieved(self):
        self.attendant.add_fuel(self.petrol)
        self.assertEqual(self.attendant.get_fuel("petrol"), self.petrol)

    def test_that_get_fuel_raises_error_for_non_string(self):
        with self.assertRaises(TypeError):
            self.attendant.get_fuel(123)

    def test_that_fuel_price_can_be_updated(self):
        self.attendant.add_fuel(self.petrol)
        self.attendant.update_fuel_price(self.petrol, 2.50)
        self.assertEqual(self.petrol.get_price_per_liter(), 2.50)

    def test_that_update_fuel_price_raises_error_for_non_fuel_object(self):
        with self.assertRaises(TypeError):
            self.attendant.update_fuel_price("petrol", 2.50)

    def test_that_fuel_can_be_restocked(self):
        self.attendant.add_fuel(self.petrol)
        self.attendant.restock_fuel(self.petrol, 100.0)
        self.assertEqual(self.petrol.get_quantity(), 150.0)

    def test_that_restock_fuel_raises_error_for_non_fuel_object(self):
        with self.assertRaises(TypeError):
            self.attendant.restock_fuel("petrol", 100.0)

    def test_that_receipt_is_stored_in_sales_records(self):
        transaction = {"fuel_type": "petrol", "liters": 10.0, "total": 655.0}
        self.attendant.generate_receipt(transaction)
        self.assertEqual(self.attendant.get_sales_records()[0], transaction)

    def test_that_empty_transaction_raises_error(self):
        with self.assertRaises(ValueError):
            self.attendant.generate_receipt({})

    def test_that_multiple_receipts_are_stored(self):
        transaction1 = {"fuel_type": "petrol", "liters": 10.0, "total": 655.0}
        transaction2 = {"fuel_type": "diesel", "liters": 20.0, "total": 1490.0}
        self.attendant.generate_receipt(transaction1)
        self.attendant.generate_receipt(transaction2)
        self.assertEqual(len(self.attendant.get_sales_records()), 2)

if __name__ == '__main__':
    unittest.main()