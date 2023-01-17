import secrets
import random
import string

def Password_Creator():

#Determine how many passwords a user wants to generate. (This would also determine how often the loop will execute).

    Number_of_Passwords = int(input("How many passwords do you want to generate? Please enter here: "))
    print()
    
#Determine the length of each password a user wants to have. 

    Length_of_Passwords = int(input("How long do you want the password(s) to be? Please enter here: "))

    print()

    print("NOTE: The passwords generated are a result of a pseudorandom formula that your computer uses.")

    print()
    
    print("As such, if you were to generate more than 10 passwords, the passwords will eventually cycle")

    print()

    print("and repeat itself. Just something to keep in mind.")

    print()

    print("Thanks. Wait one moment...")

    print()
    
# Generate a random source of string consisting of letters, numbers and special characters.

    CharacterSource = string.ascii_letters + string.digits + string.punctuation
    
# Secure the string using cryptography.

    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.punctuation)

    for i in range(256):
        password += secrets.choice(CharacterSource)

# Generating a secure random password(s).

    print("Your password(s) are:")

    print()
    
    for number in range(0,Number_of_Passwords):
        
        char_list = list(password)
        secrets.SystemRandom().shuffle(char_list)
        password = ''.join(random.choices(char_list, k = Length_of_Passwords))
        print(password)
      
Password_Creator()



