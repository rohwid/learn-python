# assuming that n is a positive integer
def fib(n):
    if n >= 3:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1

print("fib(1) = ", fib(1))
print("fib(2) = ", fib(2))
print("fib(3) = ", fib(3))
print("fib(4) = ", fib(4))
print("fib(5) = ", fib(5))
print("fib(6) = ", fib(6))
print("fib(7) = ", fib(7))
print("fib(8) = ", fib(8))
print("fib(9) = ", fib(9))
