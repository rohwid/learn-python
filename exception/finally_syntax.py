# Python program to demonstrate finally
# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)
 
# handles zerodivision exception
except Exception as err:
    print(err)
 
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')