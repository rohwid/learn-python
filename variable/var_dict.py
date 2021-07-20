dict1 = {}
dict1['one'] = "This is one"
dict1[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

## Accessing values in dictionary
print("Print dictionary on dict1['one']: ", dict1['one'])
print("Print dictionary on dict1[2]: ",dict1[2])
print("Print dictionary on dict1: ", dict1)
print("Print dictionary on tinydict: ", tinydict)
print("Print tinydict dictionary keys: ", tinydict.keys())
print("Print tinydict dictionary values: ", tinydict.values(), "\n")

## Accessing values in dictionary
dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("Print all dict2: ", dict2)
print("dict2['Name']: ", dict2['Name'])
print("dict2['Age']: ", dict2['Age'], "\n")

## Following action is not valid for tuples
# print("dict2['Zara']: ", dict2['Zara'])
# print("dict2['Alice']: ", dict2['Alice'])

## Updating dictionary
dict2['Age'] = 8
dict2['School'] = "ITS Surabaya"
print("dict2['Age']: ", dict2['Age'])
print("dict2['School']: ", dict2['School'])
print("Print all dict2: ", dict2, "\n")

## Deleting dictionary by keys
del dict2['Name']
print("Print all dict2: ", dict2, "\n")

## Follow this action will delete deictionary
# dict2.clear()
# del dict2
# print("dict['Age']: ", dict2['Age'])
# print("dict['School']: ", dict2['School'])
# print("\n")

## Property of dictionary, only print last value
dict3 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print("dict3['Name']: ", dict3['Name'])

a = 0
b = 0
c = 0
dict4 = {a: 3, b: 7, c: 9}
print("dict4[a]: ", dict4[a])
