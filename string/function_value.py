import os

def return_string():
    return "rohman"

# The string key to encrypt
# Do command before run: 
#    export SECRET_KEY="ROHMAN" 
print(f"key: {os.getenv('SECRET_KEY')}")
print(return_string())