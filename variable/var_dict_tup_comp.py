users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4ssword"),
    (3, "username", "1234")
]

print(users[2][0])

username_mapping = {user[1]: user for user in users}

print(username_mapping)
print(username_mapping["Bob"])

username_mapping = {user[0]: user for user in users}

print(username_mapping)
print(username_mapping[1])