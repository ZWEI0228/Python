
import login_system as ls         #import login_system.py, which included all the code required for login system
import os                         # import os library
import time                       # import time library
import function_box as fb         #import function_box.py module that included all the function created 

# Calling login function
# Failing to login 3 times will terminate the program
ls.login()

# Will Only Run if this is the first time opening the program
fb.initialize() # calling initialize fucntion

# Running the program until user choose to exits.
while True:
    
    try: # try running this code, until it raise error and return an error message instead of terminating program

        time.sleep(1) # Wait 1 second
        os.system('cls') # Clear the terminal
        # Displaying the title and options
        print("Inventory Management System :: Main Menu\n")
        print('1. Inventory Info Update\n2. Item Inventory Tracking\n3. Search Inventory\n4. Generate Report\n5. Hospital Details\n6. Exit')
        menu = input('> ')

        if menu == '1': 
            os.system('cls')
            menu1 = input('1. Update Item Information\n> ')

            if menu1 == '1':
                fb.listInventory() # Call listInventory fucntion
                action = input('\n1. Increase Quantity\n2. Distributing\n> ')

                if action == '1': # Prompt user for item to increase, ammount and supplier code
                    item = input("Enter the item Code you want to increase: ")
                    ammount = int(input('How much you want to increase: '))
                    supplier_code = input("Enter supplier code: ")
                    fb.increase(item, ammount,supplier_code) # Call increase fucntion with item,ammount and supplier code as arguments.

                elif action == '2': # Prompt user for item to distribute, ammount and hp_code
                    item = input("Enter the item Code you want to distribute: ")
                    ammount = int(input('How much you want to distribute: '))
                    hp_code = input("Enter Hospital Code: ") # hp = hospital
                    fb.distribute(item, ammount, hp_code) # Call increase fucntion with item,ammount and hp code as arguments.
                

        elif menu == '2':
            fb.tracking() # If user enter 2, call tracking() function 

        elif menu == '3':
            fb.search() # If user enter 3, call search() fucntion

        elif menu == '4':
            fb.report() # If user enter 4, call report() fucntion
        
        elif menu == '5':
            fb.hospital() # If user enter 5, call hostpital() fucntion

        elif menu == '6': # If user enter 6, wait 1 second and display GoodBye! message, then terminal the program.
            time.sleep(1)
            os.system('cls')
            print("GoodBye!")
            break

        else: # Tell the user that the option he/she entered is not available
            print(f"\nOption \"{menu}\" is not available.")
            time.sleep(1)
            
    except ValueError: # Error handling, return "Invalid value" if user enter an invalid value instead of crashing the program.
        print('Invalid value.')


