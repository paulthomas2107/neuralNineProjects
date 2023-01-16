import sqlite3
import datetime

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

while True:
    print("Select an option: ")
    print("1: Enter a new expense")
    print("2: View Expenses")

    choice = int(input())

    if choice == 1:
        date = input("Enter date (YYYY-MM-DD) : ")
        description = input("Enter description : ")
        cur.execute("SELECT DISTINCT category FROM expenses")
        categories = cur.fetchall()
        print("Select a category...")
        for idx, category in enumerate(categories):
            print(f"{idx + 1}. {category[0]}")
        print(f"{len(categories) + 1}. Create a new category")
        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("Enter new category name: ")
        else:
            category = categories[category_choice - 1][0]
        price = input("Enter price: ")
        cur.execute("INSERT INTO expenses (date, description, category, price) VALUES (?, ?, ?, ?)",
                    (date, description, category, price))
        conn.commit()

    elif choice == 2:
        print("Select option: ")
        print("1. View expenses")
        print("2. View monthly by category")
        view_choice = int(input())
        if view_choice == 1:
            cur.execute("SELECT * FROM expenses")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)
        elif view_choice == 2:
            month = input("Enter month (MM): ")
            year = input("Enter year (YYYY): ")
            cur.execute("SELECT category, SUM(price) FROM expenses "
                        "WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ? GROUP BY category", (month, year))

            expenses = cur.fetchall()
            for expense in expenses:
                print(f"Category: {expense[0]}, Total: {expense[1]}")
        else:
            exit()
    else:
        exit()

    repeat = input("Would you like to do something else ?  (y/n) \n")
    if repeat.lower() != "y":
        break
conn.close()


