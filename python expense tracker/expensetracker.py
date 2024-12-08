#
# ! Start display
format_output = "\033[31m"
format_reset = "\033[0m"

print(f"\n {format_output}--- Expense Tracker ---{format_reset}")

def welcome_message():
    print("\n Welcome! Ready to log, track and view your daily expenses?")

#! main app menu
def expense_tracker():
    expenses = []
    welcome_message()

    while True:
        print("\n What are we going to do? ")
        print("1. Log some expenses")
        print("2. View a full summary and breakdown of your expenses")
        print("3. Exit")

        pick = input("Type 1, 2 or 3 here to pick one: ")
        if pick == "1":
            log(expenses)
        elif pick == "2":
            summary(expenses)
        elif pick == "3":
            message()
            break
        else:
            print("Maybe that was a mistake... Please select 1, 2, or 3.")


def log(expenses):
#! Show all category options with i = number and then category
    categories = ["Food", "Utilities", "Entertainment", "Transportation", "Rent", "Savings", "Others"]
    print("\n Categories - What did you spend it on?")
    i = 1
    for category in categories:
        print(f"{i}. {category}")
        i += 1

#! Select category and display error if necessary
    while True:
        try:
            choice = int(input("Select a category by number: "))
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                break
            else:
                raise ValueError("Was that even an option? Try again...")
        except ValueError as e:
            print(f"Pretty sure you made a mistake. Try again...")

#! How much they spent
    while True:
        try:
            amount = float(input("\nEnter the amount spent: "))
            if amount <= 0:
                raise ValueError("You either just said you spent 0 or less than 0. How does that make sense? Try again...")
            break
        except ValueError:
            print(f"Was that a number? Try again...")
            continue

#! Description of expense
    description = input("\nEnter a description of what you spent money on: ")
    expenses.append({"amount": amount, "category": category, "description": description})
    print("\n Nice one! Your expense has been logged.")

#! Summary of expenses
def summary(expenses):
#! No expenses yet
    if not expenses:
        print("No expenses logged yet. Go spend some money!")
        return
#! Show full summary of all expenses and break down by category
    total_spent = sum(expense["amount"] for expense in expenses)
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
    print("\n Total Expenses:")
    print(f"\n Total amount spent: £{total_spent}")
    print("\n Amount spent by category:")
    for category, total in category_totals.items():
        print(f"For {category}, you spent: £{total}")
    print("\n All expenses:")
    i = 1
    for expense in expenses:
        print(f"{i}. £{expense['amount']} - {expense['category']} - {expense['description']}")
        i += 1

#! Exit message
def message():
    print("\n Thanks for using this tracker. See you again when you've been spending more money! \n")

expense_tracker()