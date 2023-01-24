n = 5

ex_n = n + (n - 1)
i = 1

while i <= ex_n:
    if i <= n:
        print('*' * i)
    else:
        print('*' * (n - (i % n)))
    
    i += 1