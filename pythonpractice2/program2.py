fruits = []
while True:
    fruit = input("Enter your  fruit : ")
    if fruit.lower() == 'exit':
        break
    fruits.append(fruit)


with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(f"{fruit}\n")
        print("\nfriuts are\n")
        for fruit in fruits:
            print(fruit)