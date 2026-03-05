# Dispenser.py
from multi_fuel_dispensary.Fuel import Fuel

class Dispenser:
    def __init__(self):
        self.__fuel_inventory = {}
        self.__transactions = []

    def add_fuel(self, fuel: Fuel):
        if not isinstance(fuel, Fuel):
            raise TypeError("Choose from available fuel types. (Petrol, Kerosene, Gas, Diesel)")
        self.__fuel_inventory[fuel.get_fuel_type()] = fuel

    def get_fuel(self, fuel_type: str):
        if not isinstance(fuel_type, str):
            raise TypeError("Invalid Entry. it must be in letters")
        fuel_type = fuel_type.lower().strip()
        if fuel_type not in self.__fuel_inventory:
            raise ValueError(f"Fuel type {fuel_type} not in inventory")
        return self.__fuel_inventory[fuel_type]

    def update_fuel_price(self, fuel: Fuel, price: float):
        if not isinstance(fuel, Fuel):
            raise TypeError("Invalid Entry")
        if fuel.get_fuel_type() not in self.__fuel_inventory:
            raise ValueError(f"Fuel type {fuel.get_fuel_type()} not in inventory")
        fuel.set_price_per_liter(price)

    def restock_fuel(self, fuel: Fuel, quantity: float):
        if not isinstance(fuel, Fuel):
            raise TypeError("Invalid Entry")
        if fuel.get_fuel_type() not in self.__fuel_inventory:
            raise ValueError(f"Fuel type {fuel.get_fuel_type()} not in inventory")
        fuel.set_quantity(fuel.get_quantity() + quantity)

    def dispense_fuel_by_liter(self, fuel_type: str, liters: float):
        if not isinstance(fuel_type, str):
            raise TypeError("Fuel type must be a string")
        if liters <= 0:
            raise ValueError("Liters must be greater than zero")
        fuel = self.get_fuel(fuel_type)
        if liters > fuel.get_quantity():
            raise ValueError(f"Insufficient fuel. Available: {fuel.get_quantity()} liters")
        fuel.set_quantity(fuel.get_quantity() - liters)
        total = liters * fuel.get_price_per_liter()
        return {"fuel_type": fuel_type, "liters": liters, "total": total}

    def dispense_fuel_by_amount(self, fuel_type: str, amount: float):
        if not isinstance(fuel_type, str):
            raise TypeError("Fuel type must be a string")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        fuel = self.get_fuel(fuel_type)
        liters = amount / fuel.get_price_per_liter()
        if liters > fuel.get_quantity():
            raise ValueError(f"Insufficient fuel. Available: {fuel.get_quantity()} liters")
        fuel.set_quantity(fuel.get_quantity() - liters)
        return {"fuel_type": fuel_type, "liters": liters, "total": amount}

    def store_transaction(self, transaction: dict):
        if not isinstance(transaction, dict):
            raise TypeError("Transaction must be a dict")
        if len(transaction) == 0:
            raise ValueError("Transaction must contain at least one item")
        self.__transactions.append(transaction)

    def show_all_transactions(self):
        if len(self.__transactions) == 0:
            raise ValueError("No transactions found")
        return self.__transactions