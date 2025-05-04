import sys
import csv
import bcrypt

# checklist:
# ✔ bcrypt (🤥)
# ✔ error handling (file doesnt exist)
# ✔ login logic
# ✔ password change
# ✔ register edge cases

file_name = "source.csv" #just so you dont have to type it everywhere

def main():
    # makes file if it doesnt exist
    try:
        with open(file_name, "r") as file:
            pass
    except FileNotFoundError:
        with open(file_name, "w") as file:
            pass
    # it messes up because theres an empty line at the start if you register

    # first menu that asks user to login or register or quit
    # while loop so if they type something else it asks again
    while True:
        choice = input("Login, Register or Quit? ").casefold()
        match choice:
            case "login":
                login()
                break
            case "register":
                register()
                break
            case "quit":
                print("Program quitted")
                sys.exit()
            case _:
                continue

def login():
    while True:
        username = input("Username: ")
        password = input("Password: ").encode("utf-8") #for the bcrypt to work
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for stored_user, stored_pass in reader:
                if stored_user == username and bcrypt.checkpw(password, stored_pass.encode("utf-8")):
                    print("Logged in")
                    logged_in(username)
                    return
            print("Wrong username or password")

# logged in menu that lets them change password or logout
def logged_in(username):
    while True:
        choice = input("Change password or logout? ").casefold()
        match choice:
            case "change password":
                change_password(username)
                break
            case "logout":
                print("Logged out")
                print("Program quitted")
                sys.exit()
                break
            case _:
                continue

def register():
    # check if username is alreadyu taken
    while True:
        taken = False
        username = input("Enter your username: ")
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for stored_user, _ in reader:
                if stored_user == username:
                    print("Username already taken")
                    break
            else:
                break

    password = get_password()
    hashed_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    # add credentials to the end of the file
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_pass])
        # jus so you know the file is meant to have a new line at the end

#gets a valid password from the user (>4 characters and number)
def get_password():
    while True:
        password = input("Enter your password (> 4 characters and has a number): ")
        if len(password) > 4 and any(char.isdigit() for char in password):
            return password
        else:
            print("Password must be greater than 4 characters and contain at least one number")

def change_password(username):
    password = get_password()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    # rewrites the whole file but with the password changed
    lines = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for stored_user, stored_pass in reader:
            if stored_user == username:
                lines.append([username, hashed_password])
                # the new line does bad things when its at thte end of the file ❌❌
                # and i.d.k how to fix that
            else:
                lines.append([stored_user, stored_pass])

    with open(file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerows(lines)

main()