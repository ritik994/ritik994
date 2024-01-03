def most_frequent_character(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    max_frequency = 0
    most_frequent_char = ''
    for char, count in char_count.items():
        if count > max_frequency:
            max_frequency = count
            most_frequent_char = char

    return most_frequent_char
input_string = "kkkiiiii"
result = most_frequent_character(input_string)
print(f"The most frequent character in '{input_string}' is '{result}'")