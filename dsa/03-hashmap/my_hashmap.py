class HashTable:
 
    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
 
    def create_buckets(self):
        return [[] for _ in range(self.size)]
 
    # Insert values into hash map
    def set_val(self, key, val):
       
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
        print(f'Working in index number {hashed_key}.')
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
        
        print('Here the list of the item: ')
        if bucket:
            for item in bucket:
                print(f'- {item}')
        else:
            print('- None')
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break
 
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            print(f'Value in index number {hashed_key} updated.')
            bucket[index] = (key, val)
        else:
            print(f'New value in index number {hashed_key} inserted.')
            bucket.append((key, val))
 
    # Return searched value with specific key
    def get_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break
 
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"
 
    # Remove a value with specific key
    def delete_val(self, key):
       
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
         
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
 
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
             
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
 
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
 
 
hash_table = HashTable(50)
 
# Insert some values
hash_table.set_val('rohman@gmail.com', 'qwerty123456')
print(f'Bucket: {hash_table}')
print()

# Search/access a record with key
print(hash_table.get_val('rohman@gmail.com'))
print()

# Updating the value
hash_table.set_val('rohman@gmail.com', '1234zxcv')
print(f'Bucket: {hash_table}')
print()

# Insert some values
hash_table.set_val('widiyanto@gmail.com', 'asdf1234')
print(f'Bucket: {hash_table}')
print()

# Search/access a record with key
print(f"Value of 'rohman@gmail.com' is {hash_table.get_val('rohman@gmail.com')}")
print()
 
# delete or remove a value
hash_table.delete_val('rohman@gmail.com')
print(f'Bucket: {hash_table}')

# delete or remove a value
hash_table.delete_val('widiyanto@gmail.com')
print(f'Bucket: {hash_table}')