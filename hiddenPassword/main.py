from getpass import getpass
import getch


def simple_login():
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    print(f"Connecting with username {username} and password {password}")


def getch_login(message):
    print(message, end="")
    pw = ""
    while True:
        symbol = getch.getch()
        if symbol == '\n' or symbol == '\r':
            break
        print("*", end="", flush=True)
        pw += symbol
    print()
    return pw


# simple_login()
username = input("Enter username: ")
password = getch_login("Enter password: ")
