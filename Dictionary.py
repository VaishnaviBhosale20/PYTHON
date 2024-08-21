
#dictionary

#Creating a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Dictionary:", my_dict)

#Accessing a value by key
name = my_dict['name']
print("Accessing value by key 'name':", name)

# Using get() to access a value (returns None if key doesn't exist)
age = my_dict.get('age')
print("Using get() for key 'age':", age)

# Adding a new key-value pair
my_dict['email'] = 'alice@example.com'
print("Adding a new key-value pair:", my_dict)

# Updating the value of an existing key
my_dict['age'] = 26
print("Updating value for key 'age':", my_dict)

# Removing a key-value pair using pop()
removed_value = my_dict.pop('city')
print("Removing key 'city' using pop():", my_dict, ", Removed Value:", removed_value)

# Removing the last inserted key-value pair using popitem()
last_item = my_dict.popitem()
print("Removing the last key-value pair using popitem():", my_dict, ", Last Item:", last_item)

# Checking if a key exists in the dictionary
has_key = 'name' in my_dict
print("Checking if key 'name' exists:", has_key)

# Getting all keys from the dictionary
keys = my_dict.keys()
print("All keys:", keys)

# Getting all values from the dictionary
values = my_dict.values()
print("All values:", values)

# Getting all key-value pairs as tuples using items()
items = my_dict.items()
print("All key-value pairs as tuples:", items)

# Merging two dictionaries using update()
new_data = {'job': 'Engineer', 'country': 'USA'}
my_dict.update(new_data)
print("Merging two dictionaries using update():", my_dict)

# Creating a dictionary from keys with a default value using fromkeys()
keys_list = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys_list, 0)
print("Creating a dictionary from keys with default value 0:", default_dict)

# Clearing all items from the dictionary
my_dict.clear()
print("Clearing all items from the dictionary:", my_dict)

# Copying a dictionary using copy()
copied_dict = default_dict.copy()
print("Copying the dictionary:", copied_dict)