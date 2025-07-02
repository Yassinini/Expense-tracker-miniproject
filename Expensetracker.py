print("Welcome to the expense tracker")
lists={}
current_list = None

def create_list():
    name=input("Enter a name for your new list: ")
    if name in lists:
        return name
    else:
        lists[name] = []
        print(f"List '{name}' created and selected.")
        list_name = name
def select_list():
    name=input("Enter the name of the list you'd like to select: ")
    list_name=name.lower()
    if name in lists:
        return name
    else:
        print("No such list exists, please create it first")
        return None
def add_expense(list_name):
    amount=float(input("Enter the amount: "))
    description=input("Enter the description:")
def view_expenses(list_name):
    if list_name in lists:
        print(f"Expenses for {list_name}:")
        for expense in lists[list_name]:
            print(f"{expense['description']} - ${expense['amount']}")
        else:
            print("no expenses found for this list")
def main():
    while True:
        print("\n1 create a new list")
        print("\n2 select list to work wit")
        print("\n3 add an expense")
        print("\n4 view expenses")
        print("\n5 exit")
        choice=input("Enter your choice: ")
        if choice == "1":
            create_list()
        elif choice == "2":
            select_list()
        elif choice == "3":
            add_expense(current_list)
        elif choice == "4":
            view_expenses(current_list)
        elif choice == "5":
            print("Exiting the expense tracker. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
main()