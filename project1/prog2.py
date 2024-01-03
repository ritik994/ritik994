def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
series = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = count_even_odd(series)
print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")