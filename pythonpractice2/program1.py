import random
num = random.randint(1, 1000)
while True:
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('You won!!!')
        break
    elif i < num:
               print('Try Higher')
    elif i > num:
               print('Try Lower')

print('if you gussed less than 5 times you won')