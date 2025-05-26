import os, time

credidentials = {
    'Zhen Wei': 'zhenwei123',
}

def login():
    count = 1
    while True:
        print("Inventory Management System :: Login Page\n")
        if count > 3:
            print('\nWarning: You have exceeded 3 times failure to login')
            print("Program Terminated.")
            exit()
        user_name = input("Enter you username: ")
        password = input("Enter your password: ")
        if user_name in credidentials:
            if password == credidentials[user_name]:
                print('\nLogin Successful\nloading you in...')
                break
            else:
                count += 1
                print('\nUsername or/and password is wrong.\n')
                time.sleep(1)
                os.system('cls')
        elif user_name not in credidentials:
            count += 1
            print('\nUsername or/and password is wrong.\n')
            time.sleep(1)
            os.system('cls')
    
