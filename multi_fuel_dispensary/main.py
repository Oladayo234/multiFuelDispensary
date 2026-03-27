from multi_fuel_dispensary.Fuel import Fuel
from multi_fuel_dispensary.Dispenser import Dispenser
from multi_fuel_dispensary.FuelAttendant import FuelAttendant


def display_menu():
    print("\n===== FUEL DISPENSARY SYSTEM =====")
    print("1. Add fuel to inventory")
    print("2. Restock fuel")
    print("3. Update fuel price")
    print("4. Dispense fuel by liters")
    print("5. Dispense fuel by amount")
    print("6. View inventory")
    print("7. View sales records")
    print("8. View all transactions")
    print("0. Exit")


def get_fuel_type_input():
    print("""
    1. Petrol
    2. Diesel
    3. Kerosene
    4. Gas
    """)
    try:
        choice = int(input("Enter fuel type: "))
    except ValueError:
        raise ValueError("Invalid option. Please enter a number between 1 and 4")
    if choice == 1:
        return "petrol"
    elif choice == 2:
        return "diesel"
    elif choice == 3:
        return "kerosene"
    elif choice == 4:
        return "gas"
    else:
        raise ValueError("Invalid option. Choose 1 - 4")


def add_fuel_to_inventory(attendant):
    try:
        fuel_type = get_fuel_type_input()
        quantity = float(input("Enter initial quantity (liters): "))
        price = float(input("Enter price per liter: "))
        fuel = Fuel(quantity, fuel_type, price)
        attendant.add_fuel(fuel)
        print(f"\n{fuel_type.capitalize()} added successfully!")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


def restock_fuel(attendant, dispenser):
    try:
        fuel_type = get_fuel_type_input()
        fuel = dispenser.get_fuel(fuel_type)
        quantity = float(input("Enter quantity to add (liters): "))
        attendant.restock_fuel(fuel, quantity)
        print(f"\n{fuel_type.capitalize()} restocked successfully! New quantity: {fuel.get_quantity()}L")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


def update_price(attendant, dispenser):
    try:
        fuel_type = get_fuel_type_input()
        fuel = dispenser.get_fuel(fuel_type)
        new_price = float(input("Enter new price per liter: "))
        attendant.update_fuel_price(fuel, new_price)
        print(f"\n{fuel_type.capitalize()} price updated to N{new_price}/L")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


def dispense_by_liters(attendant, dispenser):
    try:
        fuel_type = get_fuel_type_input()
        liters = float(input("Enter liters to dispense: "))
        transaction = dispenser.dispense_fuel_by_liter(fuel_type, liters)
        attendant.generate_receipt(transaction)
        dispenser.store_transaction(transaction)
        print("\n===== RECEIPT =====")
        print(f"Fuel Type: {transaction['fuel_type'].capitalize()}")
        print(f"Liters: {transaction['liters']:.2f}L")
        print(f"Total: N{transaction['total']:.2f}")
        print(f"Time: {transaction['timestamp']}")
        print("===================")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


def dispense_by_amount(attendant, dispenser):
    try:
        fuel_type = get_fuel_type_input()
        amount = float(input("Enter amount to pay: "))
        transaction = dispenser.dispense_fuel_by_amount(fuel_type, amount)
        attendant.generate_receipt(transaction)
        dispenser.store_transaction(transaction)
        print("\n===== RECEIPT =====")
        print(f"Fuel Type: {transaction['fuel_type'].capitalize()}")
        print(f"Liters: {transaction['liters']:.2f}L")
        print(f"Total: N{transaction['total']:.2f}")
        print(f"Time: {transaction['timestamp']}")
        print("===================")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


def view_inventory(dispenser):
    print("\n===== FUEL INVENTORY =====")
    fuel_types = ["petrol", "diesel", "kerosene", "gas"]
    found_any = False
    for fuel_type in fuel_types:
        try:
            fuel = dispenser.get_fuel(fuel_type)
            print(f"{fuel_type.capitalize()}: {fuel.get_quantity():.2f}L @ N{fuel.get_price_per_liter():.2f}/L")
            found_any = True
        except ValueError:
            pass
    if not found_any:
        print("No fuel in inventory")
    print("==========================")


def view_sales_records(attendant):
    sales = attendant.get_sales_records()
    if not sales:
        print("\nNo sales records found")
        return
    print("\n===== SALES RECORDS =====")
    total_sales = 0
    for item, sale in enumerate(sales, 1):
        print(f"{item}. {sale['fuel_type'].capitalize()} - {sale['liters']:.2f}L - N{sale['total']:.2f}")
        total_sales += sale['total']
    print(f"\nTotal Sales: N{total_sales:.2f}")
    print("=========================")


def view_all_transactions(dispenser):
    try:
        transactions = dispenser.show_all_transactions()
        print("\n===== ALL TRANSACTIONS =====")
        for item, transaction in enumerate(transactions, 1):
            print(f"{item}. {transaction['timestamp']} | {transaction['fuel_type'].capitalize()} - {transaction['liters']:.2f}L - N{transaction['total']:.2f}")
        print("============================")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    dispenser = Dispenser()
    attendant_name = input("Enter attendant name: ")
    try:
        attendant = FuelAttendant(attendant_name, dispenser)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return
    print(f"\nWelcome, {attendant.get_full_name()}!")
    while True:
        display_menu()
        choice = input("\nSelect option: ")
        if choice == "1":
            add_fuel_to_inventory(attendant)
        elif choice == "2":
            restock_fuel(attendant, dispenser)
        elif choice == "3":
            update_price(attendant, dispenser)
        elif choice == "4":
            dispense_by_liters(attendant, dispenser)
        elif choice == "5":
            dispense_by_amount(attendant, dispenser)
        elif choice == "6":
            view_inventory(dispenser)
        elif choice == "7":
            view_sales_records(attendant)
        elif choice == "8":
            view_all_transactions(dispenser)
        elif choice == "0":
            print("\nExiting system... Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")


if __name__ == '__main__':
    main()