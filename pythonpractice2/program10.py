class ExpenseTracker:
    def _init_(self):
        self.entries = {}

    def add_entry(self, day, amount):
        if day in self.entries:
            self.entries[day] += amount
        else:
            self.entries[day] = amount

    def remove_entry(self, day):
        if day in self.entries:
            del self.entries[day]
        else:
            print("No entry found for that day.")

    def calculate_total_spending(self):
        return sum(self.entries.values())

    def calculate_remaining_budget(self, total_income):
        total_spending = self.calculate_total_spending()
        remaining_budget = total_income - total_spending
        return remaining_budget


def main():
    
    tracker = ExpenseTracker()


    total_income = float(input("Enter your total income for the week: $"))

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add an entry")
        print("2. Remove an entry")
        print("3. Calculate total spending")
        print("4. Calculate remaining budget")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            day = input("Enter the day of the week: ").lower()
            amount = float(input("Enter the amount: $"))
            tracker.add_entry(day, amount)
            print("Entry added!")

        elif choice == '2':
            day = input("Enter the day of the week to remove entry: ").lower()
            tracker.remove_entry(day)
            print("Entry removed!")

        elif choice == '3':
            total_spending = tracker.calculate_total_spending()
            print(f"Total spending for the week: ${total_spending:.2f}")

        elif choice == '4':
            remaining_budget = tracker.calculate_remaining_budget(total_income)
            print(f"Remaining budget for the week: ${remaining_budget:.2f}")

        elif choice == '5':
            print("Exiting Expense Tracker. Have a great day!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-5).")


if _name_ == "_main_":
    main()