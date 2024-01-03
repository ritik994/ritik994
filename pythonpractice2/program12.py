def main():
    shopping_list = []

    while True:
        print("\nShopping List Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View shopping list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the shopping list.")

        elif choice == '2':
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Current Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
                index_to_remove = int(input("Enter the index of the item to remove: "))
                if 1 <= index_to_remove <= len(shopping_list):
                    removed_item = shopping_list.pop(index_to_remove - 1)
                    print(f"{removed_item} removed from the shopping list.")
                else:
                    print("Invalid index. Please enter a valid index.")

        elif choice == '3':
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Current Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")

        elif choice == '4':
            print("Exiting the Shopping List program. Have a great day!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-4).")


if __name__ == "__main__":
    main()