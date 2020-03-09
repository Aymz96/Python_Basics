# Functions
# A function is like a machine

# It can take in inputs and do some work (block of code), as well as output something different.
# They need to be called to work

# Calling a function is just writing the name and passing the argument

# Functions - Good practises
# They do one job
# They should be testable and maintainable
# Good naming convention
# Generally never print inside a function
# Inside a function your return

#### The above avoid STRING code - Spaguetti code
# Reduce technical debt

# Concept of (DRY) = Don't, Repeat, Yourself

# Seperation of concerns
# You seperate logically your code.
# Place where you define functions
# place where you write tests
# Place where you write seeds (seeds are fake data for your app)

# Syntax

#def name_of_function(arg1, arg2):
    # Block of cold
    #
    #return 'doing some work'

def say_hello_Ayman():
    return ('hello aymz')
print(say_hello_Ayman())

# Calling but not printing
# say_hello_Ayman()
#   'Hello Ayman'

# Calling and printing a function
# print(say_hello_Ayman)


def full_name_formater(f_name, l_name):
    formated_f_name = f_name.strip().capitalize()
    formated_l_name = l_name.strip().capitalize()
    # Format each name nicely
    # Can use .strip and .capitalize
    # I have access to the name via the arguments f_name and l_name
    # Save these into variabless

    # Return a joined full name that is correctly formatted
    # join the two variables into one string
    full_name = formated_f_name + ' ' +formated_l_name
    # Return said string
    return full_name
    # Call functions with name
print(full_name_formater(' ShAnnon ', 'GreyHoUnd'))

def add_funt(num1, num2):
    # I want to return the addition of two numbers
    # I have access to num1 and num2, i can add them
    # I can save the result in a variable
    result = num1 + num2
    # I can return said variable
    return result

# Calling function with two arguments
print(add_funt(10, 300))

