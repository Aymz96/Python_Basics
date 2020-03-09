# Dictionaries:

# In Python, a Dictionary can be created by placing sequence of elements within curly {} braces,
# Separated by 'comma'. Dictionary holds a pair of values,
# One being the Key and the other corresponding pair element being its Key:value.
# They are organised by index.

# We just make a list of cring_landlords, but we need more information. Like their phone numbers and address

# Example syntax:
dict_variable_name = {'key': 'value'}

boris_dict = {
    'name': 'boris',
    'l_name': 'johnson',
    'phone': '07939527648',
    'address': 'Aymz',
}

print(boris_dict)
print(type(boris_dict))

# Access one key value (Follow the same priciple as the lists, but, use keys not indexes)
print(boris_dict['name'])

last_name = boris_dict['l_name']
print(last_name)

# Change the value of on key value pair
boris_dict['phone'] = '+73425243'
print(boris_dict['phone'])

# assign a new key value pair

boris_dict['home_phone'] = ' 020834235'
print(boris_dict['home_phone'])

# get all the keys

# nested structures