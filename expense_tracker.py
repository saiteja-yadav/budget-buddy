import csv
import os
from datetime import datetime
from tabulate import tabulate

FILE_NAME = "expenses.csv"
CATEGORIES = ["Food", "Travel", "Bills", "Entertainment", "Other"]

# Create CSV file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Note"])

def add_expense():
    amount = float(input("Enter amount: ₹ "))
    category = input(f"Enter category {CATEGORIES}: ")
    note = input("Enter a note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])

    print("✅ Expense added successfully!")

def view_today_expenses():
    today = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME) as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        data = [row for row in reader if row[0] == today]
        if data:
            print(tabulate(data, headers=["Date", "Amount", "Category", "Note"]))
        else:
            print("😴 No expenses found for today.")

def monthly_total():
    month = datetime.now().strftime("%Y-%m")
    total = 0
    with open(FILE_NAME) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0].startswith(month):
                total += float(row[1])
    print(f"📆 This month's total spend: ₹{total:.2f}")

def category_stats():
    stats = {}
    with open(FILE_NAME) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[2]
            amount = float(row[1])
            stats[category] = stats.get(category, 0) + amount
    print(tabulate(stats.items(), headers=["Category", "Total Spend"]))

def export_csv():
    print(f"📤 All data is saved in '{FILE_NAME}'. You can open it with Excel or Sheets.")

def main():
    while True:
        print("\n💸 Expense Tracker CLI 💸")
        print("1. Add Expense")
        print("2. View Today's Expenses")
        print("3. View This Month's Total")
        print("4. View Spend by Category")
        print("5. Export to CSV")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_today_expenses()
        elif choice == '3':
            monthly_total()
        elif choice == '4':
            category_stats()
        elif choice == '5':
            export_csv()
        elif choice == '6':
            print("👋 Exiting... Stay frugal!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
