# Nest data structures

crazy_landl_1 = {
    'name': 'Boris',
    'phone': '078423432',
    'address_of_rent': '10 chelsea',
    'age': '28'
}

crazy_landl_2 = {
    'name': 'Filipe',
    'phone': '21243423432',
    'address_of_rent': 'Comporta, Portugal',
    'age': '28'
}

nested_dictionary = {'Boris': crazy_landl_1,
                    'filipe': crazy_landl_2
                     }
print(nested_dictionary.keys())

for key in nested_dictionary:
   print(key)
   for nest_key in nested_dictionary[key]:
   print(nest_key, nested_dictionary[key])