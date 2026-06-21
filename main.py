import csv

FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = input("Enter Amount: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense Added Successfully!\n")


def view_expenses():
    print("\n--- Expenses ---")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

    print()


def total_expense():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        for row in reader:
            total += float(row[2])

    print(f"\nTotal Expenses: ₹{total}\n")


while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice\n")
