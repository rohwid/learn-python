def named(**kwargs):
    print('kwargs: ', kwargs)
    print('named: ', kwargs['name'])
    print('age: ', kwargs['age'])

named(name="Bob", age=25)

