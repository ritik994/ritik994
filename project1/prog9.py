user_input = input("Enter a list of numbers separated by spaces: ")
user_list = list(map(int, user_input.split()))
for i in range(len(user_list) - 1, -1, -1):
    print(user_list[i])