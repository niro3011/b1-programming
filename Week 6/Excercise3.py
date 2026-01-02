#library to check the format of the entered date
from datetime import datetime

# Exercise 3: Personal Expense Tracker
# 1. Initialize Data Structures
# TODO: Create an empty list, `expense_records`, to store each expense as a tuple `(category, amount, date)`.
# Initialize an empty dictionary, `category_totals`, to sum spending by category.
# Initialize an empty set, `unique_categories`, to track all distinct categories.
expense_records = []
category_totals = {}
unique_categories = set()
#function for checking the date
def date_entry():
        while True:
            date = input(f"Enter expense {i} date (DD.MM.YYYY): ")
            try:
                parse = datetime.strptime(date, "%d.%m.%Y")
                print(f"Valid Date: {parse.strftime('%d.%m.%Y')}")
                return parse
            except ValueError:
                print("No valid date! Please try again.")

# 2. Collect Expense Data
# TODO: Implement a loop to prompt the user for 5-7 individual expenses.
# For each expense, collect the category (e.g., "Food", "Transport", "Utilities"),
# the amount (float), and the date (string, e.g., "YYYY-MM-DD").
# Store each expense as a tuple in `expense_records`.
# Example:
for i in range(1, 6): # For 5 expenses
    category = input(f"Enter expense {i} category: ")
    amount = float(input(f"Enter expense {i} amount: "))
    date = date_entry()
    expense_records.append((category, amount, date))

# 3. Categorize and Sum Expenses
# TODO: Iterate through `expense_records`.
# For each expense, add its category to `unique_categories`.
# Update the running total for that category in `category_totals`.
# If a category doesn't exist yet in the dictionary, initialize it.
# Example:
for category, amount, date in expense_records:
    unique_categories.add(category)
    category_totals[category] = category_totals.get(category, 0) + amount

# 4. Calculate Overall Statistics
# TODO: Extract all expense amounts into a separate list.
# Compute the `total_spending`, `average_expense`, `highest_expense`, and `lowest_expense`.
# Store these statistics in a separate dictionary, e.g., `overall_stats`.
# Example:
all_amounts = [amount for category, amount, date in expense_records]
total_spending = sum(all_amounts)
average_expense = total_spending / len(all_amounts) if all_amounts else 0
highest_expense = max(all_amounts) if all_amounts else 0
lowest_expense = min(all_amounts) if all_amounts else 0
#To find highest/lowest expense with category/date:
highest_expense_record = max(expense_records, key=lambda x: x[1]) if expense_records else None
lowest_expense_record = min(expense_records, key=lambda x: x[1]) if expense_records else None

# 5. Generate Spending Report
# TODO: Print a comprehensive report.
# Start with a header for "Overall Spending Summary," displaying total spending,
# average expense, and highest/lowest expense.
# Follow with "Unique Categories Spent On" (using the set).
# Finally, present "Spending by Category," iterating through `category_totals`
# and showing each category's name and total spending.
# Ensure clear formatting and appropriate currency symbols (e.g., "$").
# Example:
print("\n=== OVERALL SPENDING SUMMARY ===")
print(f"Total Spending: ${total_spending:.2f}")
print(f"Average Expense: ${average_expense:.2f}")
#if highest_expense_record:
print(f"Highest Expense: ${highest_expense_record[1]:.2f} (Category: {highest_expense_record[0]}, Date: {highest_expense_record[2]})")
#if lowest_expense_record:
print(f"Lowest Expense: ${lowest_expense_record[1]:.2f} (Category: {lowest_expense_record[0]}, Date: {lowest_expense_record[2]})")
print("\n=== UNIQUE CATEGORIES SPENT ON ===")
print(unique_categories)
print(f"Total unique categories: {len(unique_categories)}")
print("\n=== SPENDING BY CATEGORY ===")
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")