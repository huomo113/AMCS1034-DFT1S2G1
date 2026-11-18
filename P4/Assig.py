import json
import os

# Vehicle Registration Module
# Converted from the original C++ Customer Module.
# Vehicle records are saved in vehicle.dat (JSON format).

vehicles = []
DATA_FILE = "vehicle.dat"


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def load_vehicle_data():
    """Load vehicle records from the data file."""
    global vehicles

    if not os.path.exists(DATA_FILE):
        vehicles = []
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            vehicles = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Error reading vehicle.dat. Starting with an empty list.")
        vehicles = []


def store_vehicle_data():
    """Save all vehicle records to the data file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(vehicles, file, indent=4, ensure_ascii=False)
    except OSError:
        print("Error saving vehicle data.")


def create_vehicle_id():
    """Create the next available vehicle ID, for example V0001."""
    largest_number = 0

    for vehicle in vehicles:
        vehicle_id = vehicle["vehicle_id"]
        if vehicle_id.startswith("V") and vehicle_id[1:].isdigit():
            largest_number = max(largest_number, int(vehicle_id[1:]))

    return f"V{largest_number + 1:04d}"


def get_non_empty_input(prompt):
    """Ask until the user enters a value that is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value. It cannot be empty.")


def display_vehicle_details(vehicle):
    print("----------------------------------------")
    print("Vehicle ID          :", vehicle["vehicle_id"])
    print("Registration Number :", vehicle["registration_number"])
    print("Vehicle Model       :", vehicle["vehicle_model"])
    print("Owner Name          :", vehicle["owner_name"])
    print("Owner Phone         :", vehicle["owner_phone"])
    print("Owner Email         :", vehicle["owner_email"])
    print("Owner Address       :", vehicle["owner_address"])
    print("----------------------------------------")


def find_vehicle_by_id(vehicle_id):
    """Return a vehicle record when its ID is found; otherwise return None."""
    for vehicle in vehicles:
        if vehicle["vehicle_id"].lower() == vehicle_id.lower():
            return vehicle
    return None


def add_vehicle():
    clear_screen()
    print("========================================")
    print("         Register New Vehicle")
    print("========================================")

    while True:
        registration_number = get_non_empty_input(
            "Enter Vehicle Registration Number: "
        ).upper()

        # Prevent two records from using the same registration number.
        duplicate = any(
            vehicle["registration_number"].lower() == registration_number.lower()
            for vehicle in vehicles
        )
        if duplicate:
            print("This registration number is already registered.")
            continue
        break

    vehicle = {
        "vehicle_id": create_vehicle_id(),
        "registration_number": registration_number,
        "vehicle_model": get_non_empty_input("Enter Vehicle Model: "),
        "owner_name": get_non_empty_input("Enter Owner Name: "),
        "owner_phone": get_non_empty_input("Enter Owner Phone Number: "),
        "owner_email": get_non_empty_input("Enter Owner Email: "),
        "owner_address": get_non_empty_input("Enter Owner Address: ")
    }

    vehicles.append(vehicle)
    store_vehicle_data()

    print("\nVehicle registered successfully!")
    display_vehicle_details(vehicle)


def update_vehicle():
    clear_screen()
    print("========================================")
    print("          Update Vehicle Data")
    print("========================================")

    while True:
        vehicle_id = input("Enter Vehicle ID (Vxxxx): ").strip()
        vehicle = find_vehicle_by_id(vehicle_id)

        if vehicle is None:
            print("Vehicle ID not found.")
        else:
            print("\nVehicle Record:")
            display_vehicle_details(vehicle)
            print("1. Update Registration Number")
            print("2. Update Vehicle Model")
            print("3. Update Owner Name")
            print("4. Update Owner Phone")
            print("5. Update Owner Email")
            print("6. Update Owner Address")
            print("7. Update All Information")
            print("8. Return to Vehicle Menu")

            while True:
                choice = input("Enter your choice (1-8): ").strip()
                if choice in [str(number) for number in range(1, 9)]:
                    break
                print("Invalid selection. Please enter 1 to 8.")

            if choice == "8":
                return

            fields = {
                "1": ("registration_number", "Enter New Registration Number: "),
                "2": ("vehicle_model", "Enter New Vehicle Model: "),
                "3": ("owner_name", "Enter New Owner Name: "),
                "4": ("owner_phone", "Enter New Owner Phone Number: "),
                "5": ("owner_email", "Enter New Owner Email: "),
                "6": ("owner_address", "Enter New Owner Address: ")
            }

            if choice in fields:
                key, prompt = fields[choice]
                new_value = get_non_empty_input(prompt)
                if key == "registration_number":
                    new_value = new_value.upper()
                    duplicate = any(
                        item is not vehicle
                        and item["registration_number"].lower() == new_value.lower()
                        for item in vehicles
                    )
                    if duplicate:
                        print("This registration number is already used.")
                        continue
                vehicle[key] = new_value

            elif choice == "7":
                new_registration = get_non_empty_input(
                    "Enter New Registration Number: "
                ).upper()
                duplicate = any(
                    item is not vehicle
                    and item["registration_number"].lower() == new_registration.lower()
                    for item in vehicles
                )
                if duplicate:
                    print("This registration number is already used.")
                    continue

            vehicle["registration_number"] = new_registration
            vehicle["vehicle_model"] = get_non_empty_input("Enter New Vehicle Model: ")
            vehicle["owner_name"] = get_non_empty_input("Enter New Owner Name: ")
            vehicle["owner_phone"] = get_non_empty_input("Enter New Owner Phone Number: ")
            vehicle["owner_email"] = get_non_empty_input("Enter New Owner Email: ")
            vehicle["owner_address"] = get_non_empty_input("Enter New Owner Address: ")

            store_vehicle_data()
            print("\nVehicle information updated successfully!")
            display_vehicle_details(vehicle)

        again = input("\nDo you want to update another vehicle? (Y/N): ").strip().upper()
        while again not in ("Y", "N"):
            again = input("Invalid choice. Please enter Y or N: ").strip().upper()
        if again == "N":
            break


def delete_vehicle():
    clear_screen()
    print("========================================")
    print("          Delete Vehicle Data")
    print("========================================")

    while True:
        vehicle_id = input("Enter Vehicle ID: ").strip()
        vehicle = find_vehicle_by_id(vehicle_id)

        if vehicle is None:
            print("Vehicle ID not found.")
        else:
            print("\nVehicle Record:")
            display_vehicle_details(vehicle)
            confirm = input("Do you want to delete this vehicle? (Y/N): ").strip().upper()

            while confirm not in ("Y", "N"):
                confirm = input("Invalid choice. Please enter Y or N: ").strip().upper()

            if confirm == "Y":
                vehicles.remove(vehicle)
                store_vehicle_data()
                print("Vehicle deleted successfully.")
            else:
                print("Delete cancelled.")

        again = input("\nDo you want to delete another vehicle? (Y/N): ").strip().upper()
        while again not in ("Y", "N"):
            again = input("Invalid choice. Please enter Y or N: ").strip().upper()
        if again == "N":
            break


def search_vehicle():
    clear_screen()
    print("========================================")
    print("            Search Vehicle")
    print("========================================")

    while True:
        vehicle_id = input("Enter Vehicle ID: ").strip()
        vehicle = find_vehicle_by_id(vehicle_id)

        if vehicle is None:
            print("Vehicle ID not found.")
        else:
            print("\nVehicle Record:")
            display_vehicle_details(vehicle)

        again = input("\nDo you want to search another vehicle? (Y/N): ").strip().upper()
        while again not in ("Y", "N"):
            again = input("Invalid choice. Please enter Y or N: ").strip().upper()
        if again == "N":
            break


def display_vehicles():
    clear_screen()
    print("========================================")
    print("          Vehicle Registration List")
    print("========================================")

    if not vehicles:
        print("No vehicle records available.")
    else:
        for number, vehicle in enumerate(vehicles, start=1):
            print(f"\nVehicle {number}")
            display_vehicle_details(vehicle)

    input("\nPress Enter to return to the Vehicle Menu...")


def vehicle_menu():
    while True:
        print("\n========================================")
        print("          Vehicle Menu")
        print("========================================")
        print("1. Register New Vehicle")
        print("2. Update Vehicle")
        print("3. Delete Vehicle")
        print("4. Search Vehicle")
        print("5. Display All Vehicles")
        print("6. Return to Main Menu")
        print("========================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_vehicle()
        elif choice == "2":
            update_vehicle()
        elif choice == "3":
            delete_vehicle()
        elif choice == "4":
            search_vehicle()
        elif choice == "5":
            display_vehicles()
        elif choice == "6":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid selection. Please enter a number from 1 to 6.")


def main():
    load_vehicle_data()
    vehicle_menu()


if __name__ == "__main__":
    main()