def parse_kwargs(**kwargs):
    print('kwargs2: ', kwargs)
    print('named2: ', kwargs['name'])
    print('age2: ', kwargs['age'])

def named(**kwargs):
    print('kwargs1: ', kwargs)
    print('named1: ', kwargs['name'])
    print('age1: ', kwargs['age'])
    parse_kwargs(**kwargs)

named(name="Bob", age=25)

