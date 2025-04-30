import sys
import csv

def main():
    while True:
        choice = input("Login, Register or Quit? ").casefold()
        match choice:
            case "login":
                login()
                logged_in()
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
    # username part
    while True:
        found = False
        username = input("Username: ")
        with open("plain_text.txt", "r") as file:
            for line in enumerate(file):
                if line[1].split(",")[0] == username:
                    found = True
                    position = line[0]
                    break
        
        #flag thing should probably fix it coz its bad ish but it works
        if found:
            break
        else:
            print("username not found")
    

    #password part
    while True:
        found = False
        password = input("Password: ")
        with open("plain_text.txt", "r") as file:            
            #black magic but somehow i got the password from the text file
            if line[1].split(",")[1].rstrip() == password:
                found = True
                break

        if found:
            break
        else:
            print("wrong password")

def logged_in():
    while True:
        choice = input("Change password or logout? ").casefold()
        match choice:
            case "change password":
                change_password()
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
                    taken = True
                    continue
            
        if not taken:
            break

    # added it to the end
    with open("plain_text.txt", "a") as file:
        password = input("Enter your password: ")
        file.write(f"\n{username},{password}")

def change_password():
    with open("plain_text.txt", "r") as file:
        print("change password (not added)") # its here so it acutally runs
        # pseudoing my code
        # FOR line in file
        #   if line.split(",")[0].rstrip() EQUALS username
        #       line.replace(username) (⁉️)
        
        # uhh

main()