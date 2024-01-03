def display_prime_numbers(start, end):
    print(f"Prime numbers between {start} and {end}:")

    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num)
start_range = 10
end_range = 50
display_prime_numbers(start_range, end_range)