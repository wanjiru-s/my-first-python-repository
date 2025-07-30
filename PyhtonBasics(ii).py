# Conditional logic
is_old = True
is_licensed = True
if is_old:
    print("Example 1, You can drive")
elif is_licensed:
    print("You can drive now")
else:
    print("You are not old enough to drive")
# Example 2 (and statement)
if is_old and is_licensed:
    print("Example 2, You can drive")
else:
    print("You can't drive")
# Truthy and Falsy. All variables are converted into booleans once we get to if statements.
# Falsy values are like 0, none , 0.0 , an empty string, list, tuple etc.

# Ternary operator (It's a shortcut to make code cleaner)
# condition_if_true if condition else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "message denied"
print(can_message)

# Short-circuiting. You can use words like or
is_follower = True
is_user = True
if is_follower or is_user:
    print("Close friends")

# Logical operators (and, or, not, >, <, >=, <=, !=, ==)
print(5 == 5)
print(1 < 2 < 3 > 4)
print(not False)

# Exercise 1
is_magician = False
is_expert = True
# check if magician and expert: "You are a master magician"
# check if magician but not expert: "at least you're getting there"
# if you're not a magician: "You need magic powers"
if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you're getting there")
elif not is_magician:
    print("You need magic powers")

# is vs ==. the double equals checks for equality while is checks for exact match of storage in memory

# For loops. Loops allow us to run lines of code, over and over again really fast.
item: int
for item in [1, 2, 3, 4, 5, 6]:
    for x in ['a', 'b', 'c', 'd']:
        print(item, x, x, item)

# Iterables. Something you can iterate over, you can go one by one to check each item in the collection.
gamer = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
for item in gamer.items():
    print(item)
for key, value in gamer.items():
    print(key, value)
# 12 Exercise
# Build a counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
for item in my_list:
    counter = counter + item
print(counter)

# range (A special object in python)
for item in range(0, 10, 2):
    print(item, "I love you")
for _ in range(10, 0, -1):
    print(_)
for _ in range(2):
    print(list(range(1, 16)))

# Enumerate() not as common but useful. To get the index counter of an iterable
for i, char in enumerate('Hello'):
    print(i, char)
for i, var in enumerate(list(range(50))):
    if var == 50:
        print(f'index of 50 is: {i}')

# While loops. This is conditional, you must first create a variable outside the loop then use a condition.
example = 0
while example < 50:
    print(example)
    example += 1
else:
    print("Done with all the work")
# while loops are more powerful while for loops are simpler.
while True:
    response = input("say something: ")
    if response == 'bye':
        print("See you later!")
        break
# continue & pass
# first GUI
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
# iterate over picture. if 0 print '', if 1 print *
for row in picture:
    for pixel in row:
        if pixel != 1:
            print(' ', end='')
        else:
            print('*', end='')
    print('')


# Functions. After creating a defining a funciton you have to call it with the brackets.
def say_hello():
    print("Hello")


say_hello()


# Parameters and arguments. Parameters are what comes in when defining a function. It allows for arguments to be given
# when calling the function.
def say_helllo(name, emoji):
    print(f'Hellooo {name} {emoji}')


say_helllo('Angela', '🌺')


# Default parameters and Keyword Arguments
# Default parameters allow us to give parameters while defining the function.
# Keyword arguments allow us to not use positional arguments. It complicates the code
def greeting(name='Tom', emoji='🎉'):
    print(f'Helloooo {name} {emoji}')


greeting()  # With default parameters, if you do not put arguments when calling the function, it will return the default


# Return. functions always has to return something otherwise it will return none. you can have nested functions.
# Return keyword exits the function.
def addition(num1, num2):
    return num1 + num2


print(addition(6, 5))


# Methods vs functions.
# To call functions you add the brackets at the end.
# To use a method, you have to use a . Whatever is to the left of the . owns the method.


# Docstrings. You use three single quotes at the beginning and at the end to add documentation. To comment inside a
# function, to explain what a function does.

# *args **kwargs
# * args allows us to input any number/ amount of arguments we want when calling the function.
# **kwargs allows us to input any amount of key word arguments.
def super_func(*args):
    print(args)
    return sum(args)


print(super_func(1, 2, 3, 4, 5))

# Exercise.
# Create a function called highest_even that take in a list as the data type and when called, it prints out the highest
# even number.
def highest_even (li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))


# Walrus operator := It assigns values to variables as part of a larger expression.


# Scope. What variable do I have access to?
# Scope rules
# 1. Start with local
# 2. Parent local
# 3. Global scope
# 4. Built in python functions
