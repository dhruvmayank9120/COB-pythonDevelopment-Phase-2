import os
import csv
from collections import defaultdict
from datetime import datetime

# Initialize a dictionary to store expenses by category
expenses = defaultdict(float)

def record_expense():
    global expenses
    while True:
        try:
            date_str = input("Enter the expense date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, '%Y-%m-%d')
            description = input("Enter a description for the expense: ")
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: $"))

            expenses[category] += amount

            with open("expenses.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([date_str, description, category, amount])

            print("Expense recorded successfully!\n")
        except ValueError:
            print("Invalid input. Please try again.")
        finally:
            another = input("Record another expense? (y/n): ").lower()
            if another != 'y':
                break

def generate_report(month, year):
    report_filename = f"expense_report_{year}_{month}.csv"
    with open("expenses.csv", mode="r") as file, open(report_filename, mode="w", newline="") as report_file:
        reader = csv.reader(file)
        writer = csv.writer(report_file)
        writer.writerow(["Date", "Description", "Category", "Amount"])

        for row in reader:
            expense_date = datetime.strptime(row[0], '%Y-%m-%d')
            if expense_date.month == month and expense_date.year == year:
                writer.writerow(row)

    total_expenses = sum(expenses.values())

    print(f"Report generated: {report_filename}")
    print(f"Total expenses for {datetime(year, month, 1).strftime('%B %Y')}: ${total_expenses:.2f}\n")

if __name__ == "__main__":
    if not os.path.exists("expenses.csv"):
        with open("expenses.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Category", "Amount"])

    while True:
        print("Expense Tracker Menu:")
        print("1. Record an Expense")
        print("2. Generate Monthly Report")
        print("3. Exit")

        choice = input("Please select an option (1/2/3): ")

        if choice == "1":
            record_expense()
        elif choice == "2":
            try:
                month = int(input("Enter the month (1-12): "))
                year = int(input("Enter the year (e.g., 2023): "))
                generate_report(month, year)
            except ValueError:
                print("Invalid input. Please enter valid month and year.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select a valid option.\n")
