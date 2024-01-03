def divide_by_user_input():
    while True:
        try:
            user_input = float(input("Please enter a number: "))
            result = 10 / user_input
            print(f"10 divided by {user_input} is: {result}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
divide_by_user_input()