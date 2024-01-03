def count_digits(number):
    num_str = str(number)
    digit_count = len(num_str)
    return digit_count
num = 123456789
total_digits = count_digits(num)
print(f"The total number of digits in {num} is: {total_digits}")