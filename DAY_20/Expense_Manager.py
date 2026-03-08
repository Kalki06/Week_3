"""
Expense tracker CLI

A command line tool that allows user to manage personal expenses.

Features:
    - Add expenses
    - Delete expenses
    - Search expenses by category
    - See all expenses
    - calculate total spend amount

Data structure:
    - List of dictionaries storing expense records. 
"""

expenses = [
    {"id": 1, "amount": 200, "category": "Food", "description": "Lunch"},
    {"id": 2, "amount": 500, "category": "Travel", "description": "Bus ticket"},
    {"id": 3, "amount": 400, "category": "Food", "description": "Dinner"},\
]

def add_expense(expenses):
    try:
        exp_id = int(input("Enter expense id: "))
    except ValueError:
        print("Invalid input")
        return
    exp_amount = int(input("How much did you spend this time : "))
    exp_category = input("Enter the expense category : ")
    exp_description = input("Enter some description on what you spend on  : ")

    for expense in expenses:
        if(expense['id'] == exp_id):
            print("You enter wrong id \n")
            return
    
    if exp_amount <= 0:
        print("Amount must be positive")
        return
    
    user_exp = {
        "id" : exp_id,
        "amount" : exp_amount,
        "category" : exp_category,
        "description" : exp_description
    }
    
    expenses.append(user_exp)

def delete_expense(expenses):
    found = False

    try:
        exp_id = int(input("Enter expense id: "))
    except ValueError:
        print("Invalid input")
        return

    for i in range(len(expenses)):
        if(expenses[i]['id'] == exp_id):
            expenses.pop(i)
            found = True
            print("Expense deleted successfully\n")
            return

    if(found == False):
        print("Id didn't exist in your expenses.\n")


def search_category(expenses):
    found = False

    exp_category = input("Enter the category you want to see: ")

    for expense in expenses:
        if(expense["category"] == exp_category):
            print(f"ID : {expense['id']}")
            print(f"Amount : {expense['amount']}")
            print(f"Category : {expense['category']}")
            print(f"Description : {expense['description']}\n")
            found = True


    if(found == False):
        print("Category is not in the list")
    
    return


def show_all(expenses):
    if(len(expenses) == 0):
        print("Expense list is empty to add a expense please select 1.\n")
        return
    else:
        for expense in expenses:
            print(f"ID : {expense['id']}")
            print(f"Amount : {expense['amount']}")
            print(f"Category : {expense['category']}")
            print(f"Description : {expense['description']}\n")
        return

def total_expense(expenses):
    total = 0
    if(len(expenses) == 0):
        print(total)
        print("Expense list is empty to add a expense please select 1.\n")
        return
    else:
        for expense in expenses:
            total += expense["amount"]
        print(f"Total amount spend is {total}\n")
        return

def main():
    while True:
        print("Enter 1 for add")
        print("Enter 2 for delete")
        print("Enter 3 for search")
        print("Enter 4 for to show all")
        print("Enter 5 for total")
        print("Enter 6 for exit")
        print("\n")

        user_choice = input("Enter your choice here : ")
        print("\n")

        if(user_choice == "1"):
            add_expense(expenses)

        elif(user_choice == "2"):
            delete_expense(expenses)
        
        elif(user_choice == "3"):
            search_category(expenses)
        
        elif(user_choice == "4"):
            show_all(expenses)
        
        elif(user_choice == "5"):
            total_expense(expenses)
        
        elif(user_choice == "6"):
            print("Exiting.....")
            break
        else:
            print("PLEASE ENTER ONLY VALID CHOICE !!")

if __name__ == "__main__":
    main()