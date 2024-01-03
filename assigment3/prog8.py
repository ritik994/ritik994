def add_line_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    numbered_lines = [f"{idx + 1}: {line}" for idx, line in enumerate(lines)]

    with open(output_file, 'w') as file:
        file.writelines(numbered_lines)
input_filename = 'input.txt'
output_filename = 'numbered_output.txt'

add_line_numbers(input_filename, output_filename)
print(f"Line numbers have been added to '{input_filename}' and saved to '{output_filename}'.")