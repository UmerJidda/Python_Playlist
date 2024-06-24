import random

x = input('Enter a random number between 1 and 100:\n')
x = int(x)

y = random.randint(1, 100)

count = 0
while x != y:
    if x < y:
        print('The number is too low, try higher')
        x = input('Enter a random number between 1 and 100:\n')
        x = int(x)
        count += 1
    elif x > y:
        print('The number is too high, try lower')
        x = input('Enter a random number between 1 and 100:\n')
        x = int(x)
        count += 1
    else:
        print('Invalid input')
        break
print('Congrats! You guessed the number correctly!')
print(f'You guessed the number in {count} tries')

