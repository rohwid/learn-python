str1 = 'Hello World!'
str2 = "Python Programming"

## Access value
print("All str: ", str1)
print("First char of str: ", str1[0])
print("2-5 char of str: ", str1[2:5])
print("2 char till end: ", str1[2:])
print("Print two times: ", str1 * 2)
print("Joint two word: ", str1 + " Let's begin!", "\n")

## Update string
print("Updated String: ", str1[:6] + 'Python', "\n")

## String Formatting Operator
print("My name is %s and weight is %d kg!" % ('Zara', 21), "\n")

## Paragraph printing
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up."""

print(para_str)