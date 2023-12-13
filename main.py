import random
import string
import sys


def password_generator_1(length):
    charachters=string.digits
    password=''.join(random.choice(charachters) for _ in range(length))
    return password

def password_generator_2(length):
    charachters=string.ascii_letters
    password=''.join(random.choice(charachters) for _ in range(length))
    return password

def password_generator_3(length):
    charachters=string.digits+string.ascii_lowercase
    password=''.join(random.choice(charachters) for _ in range(length))
    return password
while True:
    print("1.Number only password")
    print("2.Letters only password")
    print("3.AlphaNumeric password")
    print("4.Exit")
    option = int(input("Select an option 1-4: "))

    if (option == 1):
        password_length = int(input("Enter length for password:"))
        random_password = password_generator_1(password_length)
        print("Your random password is:", random_password)
        print()
    elif (option == 2):
        password_length = int(input("Enter length for password:"))
        random_password = password_generator_2(password_length)
        print("Your random password is:", random_password)
        print()
    elif (option == 3):
        password_length = int(input("Enter length for password:"))
        random_password = password_generator_3(password_length)
        print("Your random password is:", random_password)
        print()
    elif(option==4):
        print("GoodByeee")
        sys.exit()
    else:
        print("Enter option between 1 and 4")