import datetime

# function_name = lambda param1, param2: return value
add = lambda x, y: x + y
print(add(5, 7))

# OR

print((lambda x, y: x + y)(5, 7))

# print date in ISO format
time = lambda: datetime.datetime.now().isoformat()
print(time())