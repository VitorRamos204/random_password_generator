import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    password_length = int(input("How long is the password? "))
    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Would you like a random password for your security? (Yes/No): ").capitalize()
if option == "Yes":
    generate_password()
elif option == "No":
    print("Okay, have a good day :)")
    quit()
else:
    print("Invalid option, please type Y/N")
    quit()
