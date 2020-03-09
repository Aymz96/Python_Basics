# For Loops

# syntax

# for item in iterable:
        # block of code

import time
cool_cars = ['Ferrari', 'Fiat', 'Skoda','Mk7','VW', 'focus']

#for car in cool_cars:
 #   print(car)
  #  time.sleep(1)

count = 1
for car in cool_cars:
    print(count, '-', car)
    count += 1
    time.sleep(1)

# For loop for dictionaries
boris_dict = {
    'name': 'boris',
    'l_name': 'johnson',
    'phone': '07939527648',
    'address': 'Aymz',
}
for key in boris_dict:
    print(key)

print(boris_dict['phone'])

for key in boris_dict:
    print(boris_dict['phone'])
    print(boris_dict['name'])




