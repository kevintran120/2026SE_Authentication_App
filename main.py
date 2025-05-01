import sys
import csv
import bcrypt

salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

# checklist:
# csv
# ✔ error handling (file doesnt exist)
# ✔ login logic
# ✔ password change
# ✔ register edge cases




def main():
    # makes file if it doesnt exist
    try:
        with open("plain_text.txt", "r") as file:
            pass
    except FileNotFoundError:
        with open("plain_text.txt", "w") as file:
            pass
    # it messes up because theres an empty line at the start if you register

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
        password = input("Password: ")
        with open("plain_text.txt", "r") as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(",")
                if stored_user == username and stored_pass == password:
                    print("Logged in")
                    logged_in(username)
                    return
            print("Wrong username or password")


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
    while True:
        taken = False
        username = input("Enter your username: ")
        with open("plain_text.txt", "r") as file:
            for line in file:
                if line.split(",")[0].rstrip() == username:
                    print("Username already taken")
                    break
            else:
                break

    # add it to the end
    with open("plain_text.txt", "a") as file:
        while True:
            password = input("Enter your password (> 4 characters and have a number): ")
            if len(password) > 4 and any(char.isdigit() for char in password):
                file.write(f"\n{username},{password}")
                break
            else:
                print("Password must be greater than 4 and have a number")

def change_password(username):
    while True:
        password = input("Enter your password (> 4 characters and have a number): ")
        if len(password) > 4 and any(char.isdigit() for char in password):
            break
        else:
            print("Password must be greater than 4 and have a number")

    lines = []
    with open("plain_text.txt", "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")
            if stored_user == username:
                lines.append(f"{username},{password}\n")
            else:
                lines.append(line)

    with open("plain_text.txt", "w") as file:
        for line in lines:
            file.write(line)

main()