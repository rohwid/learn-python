dict1 = {}
dict1['one'] = "This is one"
dict1[2] = "This is two"

## Accessing values in dictionary
print(f"Print dictionary on dict1['one']: {dict1['one']}")
print(f"Print dictionary on dict1[2]: {dict1[2]}")
print(f"Print dictionary on dict1: {dict1} \n")

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(f"Print dictionary on tinydict: {tinydict}")
print(f"Print tinydict dictionary keys: {tinydict.keys()}")
print(f"Print tinydict dictionary values: {tinydict.values()} \n")

## Accessing values in dictionary
dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print(f"Print all dict2: {dict2}")
print(f"dict2['Name']: {dict2['Name']}")
print(f"dict2['Age']: {dict2['Age']} \n")

## Following action is not valid for tuples
# print("dict2['Zara']: ", dict2['Zara'])
# print("dict2['Alice']: ", dict2['Alice'])

## Updating dictionary
dict2['Age'] = 8

## Add or Append new key and value
dict2['School'] = "ITS Surabaya"

print(f"dict2['Age']: {dict2['Age']}")
print(f"dict2['School']: {dict2['School']}")
print(f"Print all dict2: {dict2} \n")

## Deleting dictionary by keys
del dict2['School']

print(f"Print all dict2: {dict2} \n")

## Follow this action will delete deictionary
# dict2.clear()
# del dict2

# print(f"dict['Age']: {dict2['Age']}")
# print(f"dict['School']: {dict2['School']} \n")

## Property of dictionary, only print last value
dict3 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print(f"dict3['Name']: {dict3['Name']}")

## Variable as dict
a = 0
b = 0
c = 0
dict4 = {a: 3, b: 7, c: 9}
print("dict4[a]: {dict4[a]}")
