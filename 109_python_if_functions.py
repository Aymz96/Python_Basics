# If Functions
# Syntax

# If <condition>:
    # block of code that runs if condition returns true.
# elseif <condition>:
    # Block of code that runs if the condition is true.
# Else <condition>:
    # Block of code that runs when ALL other conditions are false.


weather = 'fish finger sandwitch'

if 'rainy' in weather:
    print('take your umbrella')
elif weather == 'sunny':
    print('Amazing day, buy an icecream')
elif weather == 'rainy':
    print('looks bad stay in')
else:
    print("Didnt quit catch that")