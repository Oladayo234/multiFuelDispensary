from multi_fuel_dispensary.Fuel import Fuel
from multi_fuel_dispensary.Dispenser import Dispenser

class FuelAttendant:
    def __init__(self, full_name: str, dispenser: Dispenser):
        self.__full_name = ""
        self.__sales_records = []
        self.__dispenser = dispenser

        self.set_full_name(full_name)

    def set_full_name(self, full_name: str):
        self.__full_name = full_name

    def get_full_name(self):
        return self.__full_name

    def get_sales_records(self):
        return self.__sales_records

    def add_fuel(self, fuel: Fuel):
        self.__dispenser.add_fuel(fuel)

    def get_fuel(self, fuel_type: str):
        self.__dispenser.get_fuel(fuel_type)

    def update_fuel_price(self, fuel: Fuel, amount: float):
        self.__dispenser.update_fuel_price(fuel, amount)

    def restock_fuel(self, fuel: Fuel,quantity: float):
        self.__dispenser.restock_fuel(fuel, quantity)

    def generate_receipt(self, transaction: dict):
        self.__sales_records.append(transaction)

