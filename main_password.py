import random
import string
from funcgenerate_password import generate_password

welcome_message = input("Welcome to your Passwordgenerator!")

option = input("For which plattform do you want to generate a password (Gmail,TikTok,Facebook..): ")

if not isinstance(option, str):
    print("Your input is invalid. Please re-enter a valid input.")
else:
    result = generate_password()
    print("\n")
    print("Your new generated " +option+ " password is: " + result) 
    quit()
   
    