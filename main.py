import string
import random

# array of all characters on keyboard
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    # Generate the password based on user input
    password_length = int(input("How long is the password? "))
    random.shuffle(characters)
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

        random.shuffle(password)

        password = "".join(password)

        print(password)


# Ask the user if he wants a password or not
option = input("Would you like a random password for your security? (Yes/No): ").capitalize()
if option == "Yes":
    generate_password()
elif option == "No":
    print("Okay, have a good day :)")
    quit()
else:
    print("Invalid option, please type Y/N")
    quit()
