def enter_word():
    while True:
        try:
            word = input("Please enter a word: ")
            if any(char.isdigit() for char in word):
                raise TypeError("You entered a number. Please enter a word.")
            if len(word) > 50:
                raise ValueError("Word length exceeds the maximum limit of 50 characters.")
            print(f"You entered the word: {word}")
            break
        except TypeError as e:
            print(f"TypeError: {e}")
        except ValueError as e:
            print(f"ValueError: {e}")
enter_word()