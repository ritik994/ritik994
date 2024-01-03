def print_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
rows = 5  
print(f"Number pattern with {rows} rows:")
print_number_pattern(rows)