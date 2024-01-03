def fibonacci_series(limit):
    num1, num2 = 0, 1
    print(num1, end=" ")
    print(num2, end=" ")
    while num2 + num1 <= limit:
        num3 = num1 + num2
        print(num3, end=" ")
        num1, num2 = num2, num3
limit = 50
print(f"Fibonacci series up to {limit}:")
fibonacci_series(limit)