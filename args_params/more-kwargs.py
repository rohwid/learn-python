def named(**kwargs):
    print(kwargs) # *kwargs as dict

def print_nicely(**kwargs):
    named(**kwargs)

    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="bob", age=25)

