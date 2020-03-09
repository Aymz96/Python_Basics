# Strings
## Strings and characters

# Syntax
# " " and ''

# Define a string

my_string = 'Hey I am a cool string B)'
# Check its type
print(type(my_string))


# Concatenation
## Adding two strings
### example 1
joint_string = my_string + 'This is another string'
print(joint_string)

# example 2
name = 'Ayman'
welcome_text = 'Welcome to DevOps'
print (welcome_text + ' ' + name)
print(welcome_text, name) # overloading the print method

# Interpolation
## Insert a string inside another string or running python inside a string
print(f'Welcome {input("What is your name?")} to class 54, we are Contested Terrain')

print('Welcome {} to class 54, we are contested terrain'.format(name))

# Useful methods
## Methods are like functions but belong to a specific data type
## For example it will not make sense if you try to capitalize integers
# example 1:
example_long_str = 'Hello this is a very bad formated text?   '

# remove trailing white spaces.
print(example_long_str.strip())

# make it lower case, make it upper case.
print(example_long_str.upper())
print(example_long_str.lower())

# make only first letter caps.
print(example_long_str.capitalize())

# make first chara of each word caps,
print(example_long_str.title())

# change the '?' into '!'
print(example_long_str.replace('?', '!'))

# change some methods and:
# remove trailing white spaces
# make it nicely formated
print(example_long_str.strip().capitalize().replace('?', "!").replace('bad', 'well'))
