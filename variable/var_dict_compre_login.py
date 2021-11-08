users = [
    {"id": 0, "username": "rohwid1", "password": "123qwe"},
    {"id": 1, "username": "rohwid2", "password": "123qwe"},
    {"id": 2, "username": "rohwid3", "password": "123qwe"},
    {"id": 3, "username": "rohwid4", "password": "123qwe"}
]

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

username_mapping = [user for user in users if user["username"] == username_input]

if username_mapping[0]["password"] == password_input:
    print("Your details are correct!")
else:
    print("Your details are incorrect!")