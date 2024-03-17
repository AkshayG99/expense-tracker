import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.dates = []

    def add_expense(self, description, amount, date):
        self.expenses.append({"description": description, "amount": amount})
        self.dates.append(date)

    def total_expenses(self):
        return sum(item["amount"] for item in self.expenses)

    def list_expenses(self):
        for item in self.expenses:
            print(f"{item['description']}: ${item['amount']}")

    def plot_expenses_over_time(self):
        plt.plot(self.dates, [item["amount"] for item in self.expenses])
        plt.xlabel('Date')
        plt.ylabel('Amount ($)')
        plt.title('Expenses Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View All Expenses")
        print("4. Plot Expenses Over Time")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            tracker.add_expense(description, amount, date)
            print("Expense added successfully!")
        elif choice == "2":
            print(f"Total expenses: ${tracker.total_expenses()}")
        elif choice == "3":
            print("\nAll Expenses:")
            tracker.list_expenses()
        elif choice == "4":
            print("\nPlotting Expenses Over Time...")
            tracker.plot_expenses_over_time()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
