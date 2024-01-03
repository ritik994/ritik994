def multiplication_table(number):
    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
num = int(input("Enter a number to print its multiplication table: "))
multiplication_table(num)