def try_param(param1, param2=None):
    if param2 == True:
        print(param1 * param1)
    else:
        print(param2)


try_param(10, param2=True)
try_param(100)
