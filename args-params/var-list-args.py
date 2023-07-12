def cacl(*args, operator=None):
    print('arg[0]: ', args[0])
    print('length of args: ', len(args))
    print('arg[1][2]: ', args[1][2])

    result = 1

    if len(args) > 3:
        print("requested paramaeter is 3")
        quit()

    if operator == "*":
        for arg in args[1]:
            result *= arg
    elif operator == "+":
        for arg in args[1]:
            result += arg
    else:
        print("Operator unknown")
        quit()

    print(result)

list_num = [1, 2, 3]
cacl("Mulitply", list_num, operator="*")