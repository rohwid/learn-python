import random

a = [56, 37, 28, 30, 37, 25, 27, 24, 35, 55, 23, 31, 55, 21, 40, 18, 50, 35, 41, 49, 37, 19, 40, 41, 31]

m = max(a)

res = [i for i, j in enumerate(a) if j == m]

if (len(res) > 1):
    sel = random.choice(res)
else:
    sel = res[0]

print(sel)