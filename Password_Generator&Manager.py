import random
import cv2

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '|', '\\', '`', '~']
password = ''
print('Welcome to your password generator and manager')
y = input('Press\n1 to generate a password\n2 to view all passwords\n3 to exit\n')
y = int(y)

if y == 1:
    x = input('Enter the length of the password:')
    x = int(x)
    for i in range(x):
        password += random.choice(list)
    site = input(str('Enter the site name:'))
    print(password)
    with open('passwords.txt', 'a') as file:
        file.write(f'{site} : {password}\n')
        file.close()
elif y == 2:
    with open('passwords.txt', 'r') as file:
        print(file.read())
        file.close()
elif y == 3:
    print('Goodbye')
    exit()

else:
    print('Invalid input')





