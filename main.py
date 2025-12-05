from src.dialectics import add_user,check_password
from src.storage import save_data,load_data


while True:
    
    try:
        print("Login 1")
        print("Register 2")
        print("Enter 0 to enter")

    
        choice = int(input("choice: "))
    except ValueError:
        print("Please enter a number")
        continue
    
    data = load_data()

    if choice == 1:
        name = str(input("name: ")).strip()
        password = input("Password: ")

        if name not in data:
            print("Uset not found")
        elif check_password(data[name], password):
            print("Login successful")
        else:
            print("Wrong password")

    elif choice == 2:
        name = str(input("name: ")).strip()
        
        if name in data:
            print(f"This name has already been entered")
            
        else:
            password = input("Password:")
            if len(password) < 6:
                print("Password must be at least 6 characters long.")
                continue
            
            if add_user(data, name, password):
                save_data(data)
                print("User saved.")
            else:
                print("This user already exists.")


    elif choice == 0:
        break

    else:
        print("The option is invalid !")