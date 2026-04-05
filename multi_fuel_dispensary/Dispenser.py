import json
import os
import datetime
from multi_fuel_dispensary.Fuel import Fuel

class Dispenser:
    FUEL_STORE = "fuel_store.txt"

    def __init__(self):
        self.__fuel_inventory = {}
        self.__transactions = []
        self.__load_fuel_store()

    def __load_fuel_store(self):
        if not os.path.exists(self.FUEL_STORE):
            return
        with open(self.FUEL_STORE, "r") as file:
            data = json.load(file)
            for fuel_type, details in data.items():
                fuel = Fuel(
                    quantity=details["quantity"],
                    fuel_type=details["fuel_type"],
                    price_per_liter=details["price_per_liter"]
                )
                self.__fuel_inventory[fuel_type] = fuel

    def __save_fuel_store(self):
        data = {}
        for fuel_type, fuel in self.__fuel_inventory.items():
            data[fuel_type] = {
                "fuel_type": fuel.get_fuel_type(),
                "quantity": fuel.get_quantity(),
                "price_per_liter": fuel.get_price_per_liter()
            }
        with open(self.FUEL_STORE, "w") as file:
            json.dump(data, file, indent=4)

    def add_fuel(self, fuel: Fuel):
        if not isinstance(fuel, Fuel):
            raise TypeError("Must be a Fuel object")
        self.__fuel_inventory[fuel.get_fuel_type()] = fuel
        self.__save_fuel_store()

    def get_fuel(self, fuel_type: str):
        if not isinstance(fuel_type, str):
            raise TypeError("Fuel type must be a string")
        fuel_type = fuel_type.lower().strip()
        if fuel_type not in self.__fuel_inventory:
            raise ValueError(f"Fuel type {fuel_type} not in inventory")
        return self.__fuel_inventory[fuel_type]

    def update_fuel_price(self, fuel: Fuel, price: float):
        if not isinstance(fuel, Fuel):
            raise TypeError("Must be a Fuel object")
        if fuel.get_fuel_type() not in self.__fuel_inventory:
            raise ValueError(f"Fuel type {fuel.get_fuel_type()} not in inventory")
        fuel.set_price_per_liter(price)
        self.__save_fuel_store()

    def restock_fuel(self, fuel: Fuel, quantity: float):
        if not isinstance(fuel, Fuel):
            raise TypeError("Must be a Fuel object")
        if fuel.get_fuel_type() not in self.__fuel_inventory:
            raise ValueError(f"Fuel type {fuel.get_fuel_type()} not in inventory")
        fuel.set_quantity(fuel.get_quantity() + quantity)
        self.__save_fuel_store()

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
        self.__save_fuel_store()
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
        self.__save_fuel_store()
        return {"fuel_type": fuel_type, "liters": liters, "total": amount}

    def store_transaction(self, transaction: dict):
        if not isinstance(transaction, dict):
            raise TypeError("Transaction must be a dict")
        if len(transaction) == 0:
            raise ValueError("Transaction must contain at least one item")
        transaction["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transactions.append(transaction)
        with open("transaction_history.txt", "a") as file:
            file.write(str(transaction) + "\n")

    def show_all_transactions(self):
        if len(self.__transactions) == 0:
            raise ValueError("No transactions found")
        return self.__transactions