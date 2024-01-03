def collatz_conjecture(n):
    print(f"Starting with n = {n}")
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1

        print(f"Current value of n: {n}")
number = int(input("Enter a positive integer to start with: "))
collatz_conjecture(number)