# Python 2.x program to demonstrate input() function
# vulnerability by passing function name as parameter
secret_value = 500

# function that returns the secret value
def secretfunction():
    return secret_value

# using raw_input() to enter the number
input1 = raw_input("Raw_input(): Guess secret number: ")

# input1 will be explicitly converted to a string
if input1 == secret_value:
    print "You guessed correct"
else:
    print "wrong answer"

# using input() to enter the number
input2 = input("Input(): Guess the secret number: ")

#input2 is evaluated as it is entered
if input2 == secret_value:
    print "You guessed correct"
else:
    print "wrong answer"
