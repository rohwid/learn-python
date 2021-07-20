def multiply(*args):
    result = 1
    
    for arg in args:
        result *= arg
    
    return result

print(multiply(1, 2, 3))