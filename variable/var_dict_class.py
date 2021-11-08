# Create your dictionary class 
class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 
  
# Main Function 
dict_obj = my_dictionary() 

data = input("Enter the Amount of Data: ")

for i in range(int(data)):
    dict_obj.key = input("Enter the key: ")
    dict_obj.value = input("Enter the value: ")
    
    dict_obj.add(dict_obj.key, dict_obj.value) 
  
print(dict_obj) 