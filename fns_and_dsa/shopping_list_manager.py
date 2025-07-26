def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            value = input("Enter a value to add ")
            shopping_list.append(value)
        elif choice == '2':
            value = input("Enter a value to remove ")
            shopping_list.remove(value)
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")