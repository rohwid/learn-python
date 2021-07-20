def multiply(*args): # The alterantive is replace the *args with the  args to parse tuple
    print(args) # *args as tuple
    
    result = 1
    
    for arg in args:
        result *= arg
    
    return result

def apply(*args, operator):
    if operator == "*":
        return multiply(*args) # The alterantive is replace the *args with the  args to parse tuple
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="*"))

