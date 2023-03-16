# function to generate - password
import string
import random

password_box = []

def generate_password():
    global password_box
    library = list(string.digits + string.ascii_letters + "!§$%&?*+#-_")
    
    
    password_length = int(input("How long would you like your password to be? "))
    
    random.shuffle(library)
    
    for x in range(password_length):
        password_box.append(random.choice(library))
    
    random.shuffle(password_box)
    
    password_box = "".join(password_box)
    
    return password_box
    
        
    
