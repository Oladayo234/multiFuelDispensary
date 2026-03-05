import unittest
from multi_fuel_dispensary.Dispenser import Dispenser
from multi_fuel_dispensary.Fuel import Fuel

class TestDispenser(unittest.TestCase):

    def setUp(self):
        self.dispenser = Dispenser()
        self.petrol = Fuel(quantity=50.0, fuel_type="petrol", price_per_liter=65.50)
        self.diesel = Fuel(quantity=50.0, fuel_type="diesel", price_per_liter=74.50)

    def test_that_dispenser_can_add_fuel(self):
        self.dispenser.add_fuel(self.petrol)
        self.assertEqual(self.dispenser.get_fuel("petrol"), self.petrol)

    def test_that_adding_same_fuel_type_updates_existing(self):
        self.dispenser.add_fuel(self.petrol)
        self.new_petrol = Fuel(quantity=50.0, fuel_type="petrol", price_per_liter=74.50)
        self.dispenser.add_fuel(self.new_petrol)
        self.assertEqual(self.dispenser.get_fuel("petrol"), self.new_petrol)

    def test_that_add_fuel_raises_error_for_non_fuel_object(self):
        with self.assertRaises(TypeError):
            self.dispenser.add_fuel("petrol")

    def test_that_get_fuel_raises_error_for_non_string(self):
        with self.assertRaises(TypeError):
            self.dispenser.get_fuel(123)

    def test_that_get_fuel_raises_error_for_unknown_fuel(self):
        with self.assertRaises(ValueError):
            self.dispenser.get_fuel("petrol")

    def test_that_fuel_price_can_be_updated(self):
        self.dispenser.add_fuel(self.petrol)
        self.dispenser.update_fuel_price(self.petrol, 40.50)
        self.assertEqual(self.petrol.get_price_per_liter(), 40.50)

    def test_that_update_fuel_price_raises_error_for_unknown_fuel(self):
        with self.assertRaises(ValueError):
            self.dispenser.update_fuel_price(self.petrol, 2.50)

    def test_that_update_fuel_price_raises_error_for_non_fuel_object(self):
        with self.assertRaises(TypeError):
            self.dispenser.update_fuel_price("petrol", 2.50)

    def test_that_fuel_can_be_restocked(self):
        self.dispenser.add_fuel(self.diesel)
        self.dispenser.restock_fuel(self.diesel, 1000.0)
        self.assertEqual(self.diesel.get_quantity(), 1050.0)

    def test_that_restock_fuel_raises_error_for_non_fuel_object(self):
        with self.assertRaises(TypeError):
            self.dispenser.restock_fuel("petrol", 1000.0)

    def test_that_restock_fuel_raises_error_for_unknown_fuel(self):
        with self.assertRaises(ValueError):
            self.dispenser.restock_fuel(self.diesel, 1000.0)

    def test_that_fuel_can_be_dispensed_by_liter(self):
        self.dispenser.add_fuel(self.petrol)
        transaction = self.dispenser.dispense_fuel_by_liter("petrol", 10.0)
        self.assertEqual(self.petrol.get_quantity(), 40.0)
        self.assertEqual(transaction["liters"], 10.0)
        self.assertEqual(transaction["total"], 655.0)

    def test_that_dispense_by_liter_raises_error_for_insufficient_fuel(self):
        self.dispenser.add_fuel(self.petrol)
        with self.assertRaises(ValueError):
            self.dispenser.dispense_fuel_by_liter("petrol", 100.0)

    def test_that_dispense_by_liter_raises_error_for_zero_liters(self):
        self.dispenser.add_fuel(self.petrol)
        with self.assertRaises(ValueError):
            self.dispenser.dispense_fuel_by_liter("petrol", 0.0)

    def test_that_fuel_can_be_dispensed_by_amount(self):
        self.dispenser.add_fuel(self.petrol)
        transaction = self.dispenser.dispense_fuel_by_amount("petrol", 655.0)
        self.assertEqual(transaction["total"], 655.0)
        self.assertEqual(transaction["fuel_type"], "petrol")

    def test_that_dispense_by_amount_raises_error_for_insufficient_fuel(self):
        self.dispenser.add_fuel(self.petrol)
        with self.assertRaises(ValueError):
            self.dispenser.dispense_fuel_by_amount("petrol", 99999.0)

    def test_that_dispense_by_amount_raises_error_for_zero_amount(self):
        self.dispenser.add_fuel(self.petrol)
        with self.assertRaises(ValueError):
            self.dispenser.dispense_fuel_by_amount("petrol", 0.0)

    def test_that_transaction_can_be_stored(self):
        transaction = {"fuel_type": "petrol", "liters": 10.0, "total": 655.0}
        self.dispenser.store_transaction(transaction)
        self.assertEqual(self.dispenser.show_all_transactions()[0], transaction)

    def test_that_empty_transaction_raises_error(self):
        with self.assertRaises(ValueError):
            self.dispenser.store_transaction({})

    def test_that_non_dict_transaction_raises_error(self):
        with self.assertRaises(TypeError):
            self.dispenser.store_transaction("transaction")

    def test_that_all_transactions_can_be_shown(self):
        transaction1 = {"fuel_type": "petrol", "liters": 10.0, "total": 655.0}
        transaction2 = {"fuel_type": "diesel", "liters": 20.0, "total": 1490.0}
        self.dispenser.store_transaction(transaction1)
        self.dispenser.store_transaction(transaction2)
        self.assertEqual(len(self.dispenser.show_all_transactions()), 2)

    def test_that_show_all_transactions_raises_error_when_empty(self):
        with self.assertRaises(ValueError):
            self.dispenser.show_all_transactions()

    def test_that_transactions_are_stored_in_order(self):
        transaction1 = {"fuel_type": "petrol", "liters": 10.0, "total": 655.0}
        transaction2 = {"fuel_type": "diesel", "liters": 20.0, "total": 1490.0}
        self.dispenser.store_transaction(transaction1)
        self.dispenser.store_transaction(transaction2)
        self.assertEqual(self.dispenser.show_all_transactions()[0], transaction1)
        self.assertEqual(self.dispenser.show_all_transactions()[1], transaction2)

if __name__ == '__main__':
    unittest.main()