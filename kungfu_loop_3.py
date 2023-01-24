def star(n):
    # assuming that n is a positive integer or 0
    if n > 1:
        print('*' * n)
        return star(n - 1)
    else:
        print('*')
        return 1

star(5)