class Fuel:
    def __init__(self, quantity:float, fuel_type:str, price_per_liter:float):
        self.quantity = 0.0
        self.__fuel_type = ""
        self.__price_per_liter = 0.0

        self.set_quantity(quantity)
        self.set_fuel_type(fuel_type)
        self.set_price_per_liter(price_per_liter)

    def set_fuel_type(self, fuel_type):
        if not isinstance(fuel_type, str):
            raise TypeError("Fuel type must be a string")
        valid_fuel_types = ("petrol", "diesel", "kerosene", "Gas")
        fuel_type = fuel_type.lower().strip()
        if fuel_type not in valid_fuel_types:
            raise ValueError(f"Invalid fuel type. Must be one of {valid_fuel_types}")
        if self.__fuel_type != fuel_type:
            self.__fuel_type = fuel_type

    def set_price_per_liter(self, price_per_liter):
        if price_per_liter <= 0.0:
            raise ValueError("Price per liter must be greater than zero")
        self.__price_per_liter = price_per_liter

    def set_quantity(self, quantity):
        if quantity < 0.0:
            raise ValueError("Quantity must be greater than zero")
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def get_fuel_type(self):
        return self.__fuel_type

    def get_price_per_liter(self):
        return self.__price_per_liter