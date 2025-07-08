user_input = "random"
data= []

def show_menu():
    print("Checklist Menu:")
    print("1. Add Item")
    print("2. Mark Item as Done")
    print("3. View Items")
    print("4. Exit")

while (user_input != "4"):
    show_menu()
    user_input = input("Please select an option: ")
    
    if user_input == "1":
        item = input("What is to be done: ")
        data.append(item)
        print("Item added",item)
    elif user_input == "2":
        item = input("What is to mark as done: ")
        if item in data:
            data.remove(item)
            print("Item marked as done:", item)
        else:
            print("Item not found in the checklist.")
            
    elif user_input == "3":
        print("Viewing all items in the checklist.")
        for item in data:
            print("-", item)

    elif user_input == "4":
        print("Exiting the checklist.")
    else:
        print("Invalid option, please try again.")


