# assuming that n is a positive integer or 0
def fact(n):
    if n >= 1:
        return n * fact(n - 1)
    else:
        return 1

print("0! = ", fact(0))
print("1! = ", fact(1))
print("2! = ", fact(2))
print("3! = ", fact(3))
print("4! = ", fact(4))
print("5! = ", fact(5))
print("6! = ", fact(6))
print("7! = ", fact(7))
print("8! = ", fact(8))
print("9! = ", fact(9))