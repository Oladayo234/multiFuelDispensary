from multi_fuel_dispensary.Fuel import Fuel
from multi_fuel_dispensary.Dispenser import Dispenser

class FuelAttendant:
    def __init__(self, full_name: str, dispenser: Dispenser):
        self.__full_name = ""
        self.__sales_records = []
        self.__dispenser = dispenser

        self.set_full_name(full_name)

    def set_full_name(self, full_name: str):
        if not isinstance(full_name, str):
            raise TypeError("Full name must be a string")
        full_name = full_name.strip()
        if len(full_name) == 0:
            raise ValueError("Full name cannot be empty")
        self.__full_name = full_name

    def get_full_name(self):
        return self.__full_name

    def get_sales_records(self):
        return self.__sales_records

    def add_fuel(self, fuel: Fuel):
        if not isinstance(fuel, Fuel):
            raise TypeError("Must be a Fuel object")
        self.__dispenser.add_fuel(fuel)

    def get_fuel(self, fuel_type: str):
        if not isinstance(fuel_type, str):
            raise TypeError("Fuel type must be a string")
        return self.__dispenser.get_fuel(fuel_type)

    def update_fuel_price(self, fuel: Fuel, price: float):
        if not isinstance(fuel, Fuel):
            raise TypeError("Must be a Fuel object")
        self.__dispenser.update_fuel_price(fuel, price)

    def restock_fuel(self, fuel: Fuel, quantity: float):
        if not isinstance(fuel, Fuel):
            raise TypeError("Must be a Fuel object")
        self.__dispenser.restock_fuel(fuel, quantity)

    def generate_receipt(self, transaction: dict):
        if not isinstance(transaction, dict):
            raise TypeError("Transaction must be a dictionary")
        if len(transaction) == 0:
            raise ValueError("Transaction cannot be empty")
        self.__sales_records.append(transaction)
        return transaction