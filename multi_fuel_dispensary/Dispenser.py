from multi_fuel_dispensary.Fuel import Fuel
class Dispenser:
    def __init__(self):
        self.__fuel_inventory = {}
        self.__transactions = []

    def add_fuel(self, fuel: Fuel):
        pass

    def get_fuel(self, fuel_type: str):
        pass

    def update_fuel_price(self, fuel: Fuel, price: float):
        pass

    def restock_fuel(self, fuel: Fuel, quantity: float):
        pass

    def dispense_fuel_by_liter(self, fuel_type: str, liters: float):
        pass

    def dispense_fuel_by_amount(self, fuel_type: str, amount: float):
        pass

    def store_transaction(self, transaction: dict):
        pass

    def show_all_transactions(self):
        pass