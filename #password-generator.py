#password-generator.py
#This program generates a random password for the user
def main():
    import random
    import string
    import pyperclip    

    length = int(input("How long do you want your password to be? "))

    while True:
        content = str(input("What do you want your password to contain(letters, numbers, numbers+letters, all)? "))
        if content == "letters":
            characters = string.ascii_letters
            break
        elif content == "numbers":
            characters = string.digits
            break
        elif content == "numbers+letters":
            characters = string.ascii_letters + string.digits
            break
        elif content == "all":
            characters = string.ascii_letters + string.digits + string.punctuation
            break
        else:
            print("Please enter a valid input")
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("This is your password: " + password)
    pyperclip.copy(password)
main()
