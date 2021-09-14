import functools

user = {"username": "jose", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permission for {user['username']}."
    
    return secure_function

@make_secure
def get_password(panel): # get_password gonna replace with secure_function
    if panel == "admin": # so this condition gonna be ignore
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_password.__name__)
print(get_password("billing"))

user = {"username": "jose", "access_level": "admin"}
print(get_password.__name__)
print(get_password("admin"))

user = {"username": "anna", "access_level": "admin"}
print(get_password.__name__)
print(get_password("billing"))