import colorama
from colorama import Fore, Style, Back
import re

# Initialize colorama
colorama.init(autoreset=True)

# Define building types with descriptions and prices
building_options = {
    "1": ("Residential House", 50000000),
    "2": ("Office Building", 120000000),
    "3": ("Shop", 30000000),
    "4": ("Warehouse", 75000000),
    "5": ("Apartment", 90000000)
}

# Helper function to validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Helper function to validate phone number (Asia region, basic validation)
def validate_phone(phone):
    pattern = r'^\+?([0-9]{10,15})$'
    return re.match(pattern, phone) is not None

# Function to display available building types and prices
def show_building_options():
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + "== Available Building Types ==")
    for key, (building_type, price) in building_options.items():
        print(Fore.YELLOW + f"{key}. {building_type}: {price:,} Kyat")

# Function to accept personal details with validations
def accept_personal_details():
    print(Fore.CYAN + "\nLet's start by gathering some information from you.\n")

    while True:
        name = input(Fore.LIGHTMAGENTA_EX + "Please enter your full name: ").strip()
        if name:
            break
        else:
            print(Fore.RED + "Name cannot be empty. Please provide a valid name.")

    while True:
        citizenship = input(Fore.LIGHTMAGENTA_EX + "Please enter your citizenship: ").strip()
        if citizenship:
            break
        else:
            print(Fore.RED + "Citizenship cannot be empty. Please provide a valid citizenship.")

    while True:
        email = input(Fore.LIGHTMAGENTA_EX + "Please enter your email address: ")
        if validate_email(email):
            break
        else:
            print(Fore.RED + "Invalid email format. Please try again.")

    while True:
        home_address = input(Fore.LIGHTMAGENTA_EX + "Please enter your home address: ")
        if home_address.strip():
            break
        else:
            print(Fore.RED + "Home address cannot be empty.")

    while True:
        phone_number = input(Fore.LIGHTMAGENTA_EX + "Please enter your phone number (Asia): ")
        if validate_phone(phone_number):
            break
        else:
            print(Fore.RED + "Invalid phone number format. Please include country code, e.g., +959123456789.")

    print(Fore.GREEN + "\nThank you! Here are the details you provided:\n")
    print(Fore.LIGHTGREEN_EX + f"Full Name: {name}")
    print(Fore.LIGHTGREEN_EX + f"Citizenship: {citizenship}")
    print(Fore.LIGHTGREEN_EX + f"Email: {email}")
    print(Fore.LIGHTGREEN_EX + f"Home Address: {home_address}")
    print(Fore.LIGHTGREEN_EX + f"Phone Number: {phone_number}\n")

    return name, citizenship, email, home_address, phone_number

# Function to accept an order from the customer
def accept_order():
    # Collect personal details first
    name, citizenship, email, home_address, phone_number = accept_personal_details()

    while True:
        show_building_options()
        choice = input(Fore.LIGHTYELLOW_EX + "\nEnter the number corresponding to the building type you'd like to order: ")

        if choice in building_options:
            building_type, price = building_options[choice]
            print(f"\n" + Fore.LIGHTGREEN_EX + f"You have selected: {building_type}")
            print(Fore.LIGHTGREEN_EX + f"Price: {price:,} Kyat")

            # Adding an advanced confirmation
            print(Fore.LIGHTBLUE_EX + "\nPlease review the details before confirming your order:")
            print(Fore.LIGHTCYAN_EX + f"Building Type: {building_type}")
            print(Fore.LIGHTCYAN_EX + f"Price: {price:,} Kyat")
            print(Fore.LIGHTCYAN_EX + f"Full Name: {name}")
            print(Fore.LIGHTCYAN_EX + f"Citizenship: {citizenship}")
            print(Fore.LIGHTCYAN_EX + f"Email: {email}")
            print(Fore.LIGHTCYAN_EX + f"Home Address: {home_address}")
            print(Fore.LIGHTCYAN_EX + f"Phone Number: {phone_number}")

            confirm = input(Fore.LIGHTYELLOW_EX + "\nWould you like to confirm this order? (yes/no): ").strip().lower()
            if confirm == 'yes':
                print(f"\n" + Fore.GREEN + Back.BLACK + Style.BRIGHT + "Thank you! Your order has been placed successfully.")
                print(Fore.LIGHTBLUE_EX + "Order Summary:")
                print(Fore.LIGHTWHITE_EX + f"Building Type: {building_type}")
                print(Fore.LIGHTWHITE_EX + f"Price: {price:,} Kyat")
                print(Fore.LIGHTWHITE_EX + f"Full Name: {name}")
                print(Fore.LIGHTWHITE_EX + f"Citizenship: {citizenship}")
                print(Fore.LIGHTWHITE_EX + f"Email: {email}")
                print(Fore.LIGHTWHITE_EX + f"Home Address: {home_address}")
                print(Fore.LIGHTWHITE_EX + f"Phone Number: {phone_number}")
                
                # Additional steps: Asking about Cloudy Messaging App
                print(Fore.LIGHTYELLOW_EX + "\nDo you know about the Cloudy Messaging App?")
                cloudy_knowledge = input(Fore.LIGHTMAGENTA_EX + "(yes/no): ").strip().lower()
                
                if cloudy_knowledge == 'yes':
                    print(Fore.CYAN + "Great! Have you tried it out yet?")
                    tried_cloudy = input(Fore.LIGHTMAGENTA_EX + "(yes/no): ").strip().lower()
                    if tried_cloudy == 'yes':
                        print(Fore.GREEN + "Awesome! We're glad you're using it!")
                    else:
                        print(Fore.CYAN + "You should definitely give it a try! It's a great way to stay connected.")
                else:
                    print(Fore.CYAN + "Cloudy Messaging App is an amazing platform to stay connected with people. You should check it out!")
                
                # Add fact about Cloudy's creator
                print(Fore.LIGHTBLUE_EX + "\nThat Cloudy's creator is Dominex (Nyi Nyi Linn Htet), 18 years old boy.")
                break
            else:
                print(Fore.LIGHTRED_EX + "\nOrder not confirmed. You can select another building type.\n")
        else:
            print(Fore.RED + "Invalid option, please try again.")

# Main program
if __name__ == "__main__":
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "=== Welcome to the Advanced Carpenter's Building Order System ===\n")
    accept_order()
