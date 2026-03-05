from unittest import TestCase
from multi_fuel_dispensary.Fuel import Fuel

class TestFuel(TestCase):
    def setUp(self):
        self.fuel = Fuel(quantity = 50.0, fuel_type = "Petrol", price_per_liter = 1.50)

    def test_that_fuel_that_fuel_can_be_created_with_correct_inputs(self):
        self.assertEqual(self.fuel.quantity, 50.0)
        self.assertEqual(self.fuel.get_fuel_type(), "petrol")
        self.assertEqual(self.fuel.get_price_per_liter(), 1.50)

    def test_that_invalid_fuel_type_raises_error(self):
        with self.assertRaises(ValueError):
            self.fuel.set_fuel_type("Gasoline")

    def test_that_invalid_price_raises_error(self):
        with self.assertRaises(ValueError):
            self.fuel.set_price_per_liter(-1.0)

    def test_that_zero_price_raises_error(self):
        with self.assertRaises(ValueError):
            self.fuel.set_price_per_liter(0.0)

    def test_that_negative_quantity_raises_error(self):
        with self.assertRaises(ValueError):
            self.fuel.set_quantity(-10.0)

    def test_that_quantity_can_be_set_to_zero(self):
        self.fuel.set_quantity(0.0)
        self.assertEqual(self.fuel.get_quantity(), 0.0)

    def test_that_fuel_type_can_be_updated(self):
        self.fuel.set_fuel_type("Diesel")
        self.assertEqual(self.fuel.get_fuel_type(), "diesel")

    def test_that_price_can_be_updated(self):
        self.fuel.set_price_per_liter(2.50)
        self.assertEqual(self.fuel.get_price_per_liter(), 2.50)

    def test_that_quantity_can_be_updated(self):
        self.fuel.set_quantity(100.0)
        self.assertEqual(self.fuel.get_quantity(), 100.0)

