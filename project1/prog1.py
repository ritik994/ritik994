def print_pattern(rows):
    for i in range(1, rows * 2):
        if i <= rows:
            for j in range(1, i + 1):
                print("*", end=" ")
        else:
            for j in range(1, (rows * 2) - i + 1):
                print("*", end=" ")
        print()
rows = 5
print(f"Pattern with {rows} rows:")
print_pattern(rows)