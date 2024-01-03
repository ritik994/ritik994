import re
def extract_numbers(text):
    numbers_list = re.findall(r'\d+', text)
    return numbers_list
input_string = "Hello 123 World 456"
numbers = extract_numbers(input_string)
print("Numbers extracted from the string:", numbers)