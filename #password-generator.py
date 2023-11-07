#password-generator.py
#This program generates a random password for the user
def main():
    import random
    import string
    import pyperclip
    #Get user input for password length
    length = int(input("How long do you want your password to be? "))
    while True:
        content = str(input("What do you want your password to contain(letters, numbers, all)? "))
        if content == "letters":
            characters = string.ascii_letters
            break
        elif content == "numbers":
            characters = string.ascii_letters + string.digits
            break
        elif content == "all":
            characters = string.ascii_letters + string.digits + string.punctuation
            break
        else:
            print("Please enter a valid input")
    #Create a password variable
    password = ""
    #Create a loop to generate a random password
    for i in range(length):
        password += random.choice(characters)
    #Print the password
    print("This is your password: " + password)
    pyperclip.copy(password)
main()