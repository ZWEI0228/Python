

import os # Import os module
import time # Import time module
from datetime import datetime # Import datetime from datetime

# test if the module if properly imported
def testing():
    print("Testing 1..2..")

# Create PPE.txt file for storing ppe information for first time initialize the program
def initialize():
    file_path_ppe = "ppe.txt"
    file_path_suppliers = "suppliers.txt"

    # Check if ppe.txt and suppliers.txt exist, create if not
    if not os.path.exists(file_path_ppe) or not os.path.exists(file_path_suppliers):
        print("Initial Inventory Creation")
        print('\nYou\'re seeing this message because this is the first time you initialized the program.\n')
        
        # Create ppe.txt if it does not exist
        if not os.path.exists(file_path_ppe):
            with open(file_path_ppe, 'w') as file_ppe:
                print("Inserting item details: \n")
                while True: 
                    # Prompt user for item details for creating item in ppe.txt
                    item_code = input("Enter Item Code: ").strip()
                    supplier_code = input("Enter Supplier Code: ").strip()
                    item_name = input("Enter Item Name: ").strip()
                    quantity = 100
                    file_ppe.write(f"{item_code},{supplier_code},{item_name},{quantity}\n")
                    print("Added Successfully.\nWould you like to continue adding (Yes/No)?")
                    user = input('> ').lower()
                    if user != 'yes':
                        break

        # Create suppliers.txt if it does not exist
        if not os.path.exists(file_path_suppliers):
            with open(file_path_suppliers, 'w') as file_suppliers:
                file_suppliers.write("SupplierCode,ItemCode,Amount,Month\n")
        
        # Automatically record supplier details based on input provided for ppe.txt
        with open(file_path_ppe, 'r') as file_ppe:
            lines = file_ppe.readlines()
        
        # Automatically record supplier details based on input provided for ppe.txt
        with open(file_path_suppliers, 'a') as file_suppliers:
            current_month = datetime.now().strftime("%Y-%m") # Record curent month and year
            for line in lines:
                item_code, supplier_code, item_name, quantity = line.strip().split(',')
                file_suppliers.write(f"{supplier_code},{item_code},{quantity},{current_month}\n")
    else:
        pass


# List everything in the inventory or ppe.txt file
def listInventory():
    time.sleep(1)
    os.system("cls")
    print("Inventory Management System :: Inventory\n")
    print("[Item Code, Supplier Code, Item Name, Quantity]")
    fhand = open("ppe.txt")
    for line in fhand:
        line = line.rstrip()
        lst = line.split(',')
        print(lst)

def listSupplier(): # This function list out all the supplier details
    time.sleep(1)
    os.system("cls")
    print("Inventory Management System :: Supplier Details\n")
    print("[Supplier Code, Name, Address]")
    fhand = open("suppliers.txt")
    for line in fhand:
        line = line.rstrip()
        lst = line.split(',')
        print(lst)


def increase(item, amount, supplier_code):
    # Read the inventory file
    with open('ppe.txt', 'r') as fhand:
        lines = fhand.readlines()
    
    modified_lines = []
    for line in lines:
        if line.startswith(item):
            line = line.rstrip()
            lst = line.split(',')
            lst[3] = str(int(lst[3]) + amount)
            modified_line = ','.join(lst) + '\n'
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)
    
    # Write the updated inventory back to the file
    with open('ppe.txt', 'w') as fhand:
        fhand.writelines(modified_lines)
    
    print("Inventory Updated Successfully.")

    # Record supplier information
    current_month = datetime.now().strftime('%Y-%m')
    supplier_record = f"{supplier_code},{item},{amount},{current_month}\n"

    # Check if supplier.txt exists and create if it doesn't
    if not os.path.exists('suppliers.txt'):
        with open('suppliers.txt', 'w') as fhand:
            fhand.write("SupplierCode,ItemCode,Amount,Month\n")
    
    # Append the new supplier record
    with open('suppliers.txt', 'a') as fhand:
        fhand.write(supplier_record)

    print("Supplier information recorded successfully.")
    

def distribute(item, amount, hp_code):
    # Read the inventory file
    with open('ppe.txt', 'r') as fhand:
        lines = fhand.readlines()

    modified_lines = []
    distributed = False
    hospital_code = hp_code

    for line in lines:
        if line.startswith(item):
            line = line.rstrip()
            lst = line.split(',')

            if amount <= int(lst[3]):
                lst[3] = str(int(lst[3]) - amount)
                modified_line = ','.join(lst) + '\n'
                modified_lines.append(modified_line)
                distributed = True
            else:
                print(f"You only have {lst[3]} boxes left, unable to distribute {amount} boxes.")
                input("Press \"Enter\" to continue.")
                break
        else:
            modified_lines.append(line)

    if distributed:
        # Update the inventory file
        with open('ppe.txt', 'w') as fhand:
            fhand.writelines(modified_lines)

        print("Inventory Updated Successfully.")

        # Record the current month
        current_month = datetime.now().strftime('%Y-%m')

        # Check if distribution.txt exists and read its contents
        distribution_records = {}
        if os.path.exists('distribution.txt'):
            with open('distribution.txt', 'r') as fhand:
                for line in fhand:
                    hosp_code, dist_item, qty, month = line.strip().split(',')
                    qty = int(qty)
                    if (hosp_code, dist_item) in distribution_records:
                        distribution_records[(hosp_code, dist_item)] += qty
                    else:
                        distribution_records[(hosp_code, dist_item)] = qty

        # Update the distribution record
        if (hospital_code, item) in distribution_records:
            distribution_records[(hospital_code, item)] += amount
        else:
            distribution_records[(hospital_code, item)] = amount

        # Write the updated records back to distribution.txt
        with open('distribution.txt', 'w') as fhand:
            for (hosp_code, dist_item), qty in distribution_records.items():
                fhand.write(f"{hosp_code},{dist_item},{qty},{current_month}\n")

        print("Distribution Record Updated Successfully.")

        input("Press \"Enter\" to continue.")


# Function for tracking inventory stock
def tracking():
    with open('ppe.txt', 'r') as fhand:
        lines = fhand.readlines()

    inventory = []

    # Read line by line of items in ppe, split each item details into item_code and quantity
    for line in lines:
        line = line.rstrip()
        lst = line.split(',')
        item_code = lst[0]
        quantity = int(lst[3])
        inventory.append((item_code, quantity))

    print("\nItem Inventory Tracking")
    print("1. Total available quantity of all items sorted in ascending order by item code.")
    print("2. Records of all items that have stock quantity less than 25 boxes.")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        inventory.sort() # sorting item alphabetically and display them
        print("\nTotal available quantity of all items sorted by item code:")
        for item_code, quantity in inventory:
            print(f"{item_code}: {quantity} boxes")
        input("Press \"Enter\" to continue.") # Waiting until user press enter

    elif choice == '2': # Display all items with stock quantity less than 25 boxes
        print("\nRecords of all items with stock quantity less than 25 boxes:")
        for item_code, quantity in inventory:
            if quantity < 25:
                print(f"{item_code}: {quantity} boxes")
        input("Press \"Enter\" to continue.") # Waiting until user press enter
    else:
        print("Invalid choice. Please enter 1 or 2.")
        input("Press \"Enter\" to continue.") # Waiting until user press enter

# Searching function
def search():
    item_code = input("Enter the Item Code to search: ").strip()
    
    if not os.path.exists('distribution.txt'): # Check if the file exists, if not return nothing instead of crashing
        print("No distribution records found.")
        input("Press \"Enter\" to continue.")
        return

    distribution_records = {} # Create empty dictionary

    # Read the distribution file
    with open('distribution.txt', 'r') as fhand:
        for line in fhand:
            hosp_code, dist_item, qty, month = line.strip().split(',')
            qty = int(qty)
            if dist_item == item_code:
                if hosp_code in distribution_records:
                    distribution_records[hosp_code] += qty
                else:
                    distribution_records[hosp_code] = qty

    if distribution_records:
        print(f"\nDistribution list for item {item_code}:")
        for hosp_code, qty in distribution_records.items():
            print(f"Hospital Code: {hosp_code}, Quantity Distributed: {qty} boxes")
    else:
        print(f"No distribution records found for item {item_code}.")

    input("Press \"Enter\" to continue.")


# Function to:
# list of suppliers with their PPE equipments supplied.
# List of hospitals with quantity of distribution items.
# Overall transaction report for a selected month.
def report():
    print("Report Options")
    print("1. List of suppliers with their PPE equipments supplied.")
    print("2. List of hospitals with quantity of distribution items.")
    print("3. Overall transaction report for a selected month.")
    choice = input("Choose an option (1, 2, or 3): ")

    if choice == '1':
        if not os.path.exists('suppliers.txt'): # Check if the file exists, if not return nothing instead of crashing
            print("No supplier records found.")
            input("Press \"Enter\" to continue.")
            return

        suppliers = {}
        with open('suppliers.txt', 'r') as fhand:
            next(fhand)  # Skip the header line
            for line in fhand: # Read the file line by line then split item based on seperated by comma
                supplier_code, item_code, amount, month = line.strip().split(',')
                amount = int(amount)
                if supplier_code in suppliers: # Check if the supplier code is in suppliers.txt, if yes append into suppliers based on supplier code
                    suppliers[supplier_code].append((item_code, amount, month))
                else:
                    suppliers[supplier_code] = [(item_code, amount, month)]

        print("\nList of suppliers with their PPE equipment supplied:")
        for supplier_code, items in suppliers.items():
            print(f"Supplier Code: {supplier_code}")
            for item_code, amount, month in items:
                print(f"  Item: {item_code}, Amount: {amount}, Month: {month}")
    
    elif choice == '2':
        if not os.path.exists('distribution.txt'): # Check if the file exists, if not return nothing instead of crashing
            print("No distribution records found.")
            input("Press \"Enter\" to continue.")
            return

        hospitals = {}
        with open('distribution.txt', 'r') as fhand:
            for line in fhand:
                hospital_code, item_code, amount, month = line.strip().split(',')
                amount = int(amount)
                if hospital_code in hospitals:
                    if item_code in hospitals[hospital_code]:
                        hospitals[hospital_code][item_code] += amount
                    else:
                        hospitals[hospital_code][item_code] = amount
                else:
                    hospitals[hospital_code] = {item_code: amount}

        print("\nList of hospitals with quantity of distribution items:")
        for hospital_code, items in hospitals.items():
            print(f"Hospital Code: {hospital_code}")
            for item_code, amount in items.items():
                print(f"  Item: {item_code}, Amount: {amount}")

    elif choice == '3':
        selected_month = input("Enter the month (YYYY-MM) to generate the report for: ").strip()

        if not os.path.exists('suppliers.txt') and not os.path.exists('distribution.txt'):
            print("No records found.")
            input("Press \"Enter\" to continue.")
            return

        suppliers = {}
        if os.path.exists('suppliers.txt'):
            with open('suppliers.txt', 'r') as fhand:
                next(fhand)  # Skip the header line
                for line in fhand:
                    supplier_code, item_code, amount, month = line.strip().split(',')
                    if month == selected_month:
                        amount = int(amount)
                        if supplier_code in suppliers:
                            if item_code in suppliers[supplier_code]:
                                suppliers[supplier_code][item_code] += amount
                            else:
                                suppliers[supplier_code][item_code] = amount
                        else:
                            suppliers[supplier_code] = {item_code: amount}

        hospitals = {}
        if os.path.exists('distribution.txt'):
            with open('distribution.txt', 'r') as fhand:
                for line in fhand:
                    hospital_code, item_code, amount, month = line.strip().split(',')
                    if month == selected_month:
                        amount = int(amount)
                        if hospital_code in hospitals:
                            if item_code in hospitals[hospital_code]:
                                hospitals[hospital_code][item_code] += amount
                            else:
                                hospitals[hospital_code][item_code] = amount
                        else:
                            hospitals[hospital_code] = {item_code: amount}

        print(f"\nOverall transaction report for {selected_month}:")
        if suppliers:
            print("\nSupplies received from suppliers:")
            for supplier_code, items in suppliers.items():
                print(f"Supplier Code: {supplier_code}")
                for item_code, amount in items.items():
                    print(f"  Item: {item_code}, Amount: {amount}")
        else:
            print("No supplies received from suppliers.")

        if hospitals:
            print("\nDistributions to hospitals:")
            for hospital_code, items in hospitals.items():
                print(f"Hospital Code: {hospital_code}")
                for item_code, amount in items.items():
                    print(f"  Item: {item_code}, Amount: {amount}")
        else:
            print("No distributions to hospitals.")

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    input("Press \"Enter\" to continue.")

# This function resonsible for adding or modify existing hospotal details
def hospital():
    # Check if hospital.txt exists, create it if it does not
    if not os.path.exists('hospital.txt'):
        with open('hospital.txt', 'w') as fhand:
            fhand.write("HospitalCode,HospitalName,Address\n")
    
    print("Hospital Options")
    print("1. Add New Hospital")
    print("2. Modify Existing Hospital Details")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        add_new_hospital()
    elif choice == '2':
        modify_existing_hospital()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        input("Press \"Enter\" to continue.")

def add_new_hospital(): # This function resonsible for adding hospotal details
    hospital_code = input("Enter Hospital Code: ").strip()
    hospital_name = input("Enter Hospital Name: ").strip()
    address = input("Enter Address: ").strip()

    # Append the new hospital details to hospital.txt
    with open('hospital.txt', 'a') as fhand:
        fhand.write(f"{hospital_code},{hospital_name},{address}\n")

    print("New hospital added successfully.")
    input("Press \"Enter\" to continue.")

def modify_existing_hospital(): # This function resonsible for modify existing hospotal details
    hospital_code = input("Enter Hospital Code of the hospital to modify: ").strip()

    with open('hospital.txt', 'r') as fhand:
        lines = fhand.readlines()

    modified_lines = []
    found = False
    for line in lines:
        if line.startswith(hospital_code):
            found = True
            print("Current details:")
            print(line.strip())
            hospital_name = input("Enter new Hospital Name: ").strip()
            address = input("Enter new Address: ").strip()
            modified_line = f"{hospital_code},{hospital_name},{address}\n"
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)

    if found:
        with open('hospital.txt', 'w') as fhand:
            fhand.writelines(modified_lines)
        print("Hospital details modified successfully.")
    else:
        print(f"No hospital found with the code {hospital_code}.")

    input("Press \"Enter\" to continue.")






















