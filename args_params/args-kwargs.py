def both(*args, **kwargs):
    print(args)
    print(kwargs)
    print(len(args))
    print(len(kwargs))

both(1, 3, 5, name="bob", age=25)