import random
import hashlib

characters = (
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '0123456789'
    '!@#$%^&*()-_=+[]{};:\'",.<>?/|\\`~'
)


def generate_password(length):
    return ''.join(random.choice(characters) for _ in range(length))


def hash_password(password):
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature


def save_password(site, password):
    with open('passwords.txt', 'a') as file:
        hashed_password = hash_password(password)
        file.write(f'{site} : {hashed_password}\n')


def view_passwords():
    try:
        with open('passwords.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("No passwords saved yet.")


def main():
    print('Welcome to your password generator and manager')

    while True:
        try:
            choice = int(input('Press\n1 to generate a password\n2 to view all passwords\n3 to exit\n'))

            if choice == 1:
                length = int(input('Enter the length of the password: '))
                password = generate_password(length)
                site = input('Enter the site name: ')
                print(f'Generated password: {password}')
                save_password(site, password)

            elif choice == 2:
                view_passwords()

            elif choice == 3:
                print('Goodbye')
                break

            else:
                print('Invalid input. Please choose a valid option.')

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
