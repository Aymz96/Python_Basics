# Variables
## - A Python variable is a reserved memory location to store values. In other words, a variable in a python program gives data to the computer for processing.
## Every value in Python has a datatype.  Different data types in Python are Numbers, List, Tuple, Strings, Dictionary, etc.

book = 'Rich dad, poor dad'

# Print Function
## - The print() function prints the specified message to the screen, or other standard output device.
## The message can be a string, or any other object, the object will be converted into a string before written to the screen.

book
print(book)

# Type Function
## type() method returns class type of the argument(object) passed as parameter. type() function is mostly used for debugging purposes.

data_type_of_book = type(book)
print(data_type_of_book)

# Input Function input()- prompts user for input
# You can add a string to the argument so it prints that before capturing the input
input('Please input something to execute')

# Conventions
## lower case for variable naming with under score