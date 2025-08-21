identity = 'John'
print(f'Hello {identity}, would you like to learn some python today?')
print(identity.lower())
print(identity.upper())
print(identity.title())
author = 'Emily Dickinson'
famous_quote = "Believe you can and you're halfway there"
print(f'{author} once said, "{famous_quote}"')
famous_person = 'nelson mandela'
famous_person = famous_person.title()
print(famous_person)
message = f'{famous_person} once said\n\t "Survival for the fittest"'
print(message)
print(famous_person.replace('Nelson Mandela', 'Dedan Kimathi'))
print(famous_person)
famous_person = famous_person.replace('Nelson Mandela', 'Dedan Kimathi')
print(famous_person)
print(message)
my_name = ' sharon '
print(my_name)
print(my_name.lstrip())
print(my_name.rstrip())
print(my_name.title().strip())
favorite_number = 9
print(10 - 2)
print(16 / 2)
print(6 + 2)
print(4 * 2)
print(f'My favorite number is {favorite_number}')

# import this

names = ['Emily', 'Nicole', 'Tevin', 'Andria', 'Michael']
print(names)
print(names[4])
print(names[0])
print(names[1])
print(names[3])
print(names[2])
print(f"What's poppin' {names[4]} ?")
print(f"What's poppin' {names[0]} ?")
print(f"What's poppin' {names[1]} ?")
print(f"What's poppin' {names[3]} ?")
print(f"What's poppin' {names[2]} ?")

dream_cars = ['Lambo', 'G Wagon', 'Range']
print(f'I would love to own a {dream_cars[0]} soon 💃')
print(f'I would love to own a {dream_cars[1]} soon 🎉')
print(f'I would love to own a {dream_cars[2]} soon 🤸‍♀️')

guest_list = ['Shenseea', 'Rihana', 'Kim Kardashian', 'Burna Boy', 'Davido']
print(f'{guest_list[0]}, you are invited to dine with me'
      f'\n{guest_list[1]}, you are inited to dine with me'
      f'\n{guest_list[2]}, you are invited to dine with me'
      f'\n{guest_list[3]}, you are invited to dine with me'
      f'\n{guest_list[4]}, you are invited to dine with me')
print(guest_list[3])
absent = guest_list.pop(3)
print(guest_list)
guest_list.insert(3, 'Taves')
print(guest_list)
print(f'{guest_list[0]}, you are invited to dine with me'
      f'\n{guest_list[1]}, you are inited to dine with me'
      f'\n{guest_list[2]}, you are invited to dine with me'
      f'\n{guest_list[3]}, you are invited to dine with me'
      f'\n{guest_list[4]}, you are invited to dine with me')
print('I found a bigger dinner table!')
guest_list.insert(0, 'Kai')
guest_list.insert(3, 'Odumodu')
guest_list.append('Kanye West')
print(f'{guest_list[0]}, you are invited to dine with me'
      f'\n{guest_list[1]}, you are inited to dine with me'
      f'\n{guest_list[2]}, you are invited to dine with me'
      f'\n{guest_list[3]}, you are invited to dine with me'
      f'\n{guest_list[4]}, you are invited to dine with me'
      f'\n{guest_list[5]}, you are invited to dine with me'
      f'\n{guest_list[6]}, you are invited to dine with me'
      f'\n{guest_list[7]}, you are invited to dine with me')
print("I'm sorry I can only invite 2 people for dinner 😪")
print(guest_list)
absentee7 = guest_list.pop()
print(f'I am sorry I can not invite {absentee7} to dinner')
absentee6 = guest_list.pop(6)
print(f'I am sorry I can not invite {absentee6} to dinner')
absentee4 = guest_list.pop(4)
print(f'I am sorry I can not invite {absentee4} to dinner')
absentee3 = guest_list.pop(3)
print(f'I am sorry I can not invite {absentee3} to dinner')
absentee2 = guest_list.pop(2)
print(f'I am sorry I can not invite {absentee2} to dinner')
absentee0 = guest_list.pop(0)
print(f'I am sorry I can not invite {absentee0} to dinner')
print(guest_list)
print(f'{guest_list[0]}, you ae still invited to dinner 😀'
      f'\n{guest_list[1]}, you are still invited to dinner 😁')
# del guest_list[0]
# del guest_list[1]
print(guest_list)

dream_countries = ['Greece', 'Monaco', 'Japan']
print(dream_countries)
print(sorted(dream_countries))
print(dream_countries)
print(sorted(dream_countries, reverse=True))
print(dream_countries)
dream_countries.reverse()
print(dream_countries)
dream_countries.reverse()
print(dream_countries)
dream_countries.sort()
print(dream_countries)
dream_countries.sort(reverse=True)
print(dream_countries)
print(len(guest_list))

african_countries = ['Kenya', 'South Africa', 'Egypt', 'Mauritius', 'Ghana', 'Rwanda', 'Nigeria']
print(african_countries)
african_countries.append('Togo')
print(african_countries)
african_countries.insert(3, 'Zimbabwe')
print(african_countries)
eliminated_country = african_countries.pop(0)
print(f'I am sorry {eliminated_country}, you have been cast out of Africa')
print(african_countries)
print(sorted(african_countries))
print(african_countries)
african_countries.reverse()
print(african_countries)
african_countries.sort()
print(african_countries)
african_countries.reverse()
print(african_countries)
print(sorted(african_countries))
print(sorted(african_countries, reverse=True))
print(len(african_countries))
del african_countries[-1]
print(len(african_countries))

# Chapter 4
pizzas = ['Hawaian', 'Chicken bbq', 'Peri peri']
for flavor in pizzas:
    print(flavor)
for flavor in pizzas:
    print(f'I like {flavor} pizza!')
print('I really love pizza')

fishes = ['Salmon', 'Tilapia', 'Nile Perch']
for fish in fishes:
    print(fish)
for fish in fishes:
    print(f'{fish}, is a very good source of lean protein.')
print('Pick any of these fish as your main source of protein')

for number in range(1, 21):
    print(number)

hundreds = list(range(1, 101))
for number in hundreds:
    print(number)
print(min(hundreds), max(hundreds), sum(hundreds))

odds = list(range(1, 21, 2))
for number in odds:
    print(number)

multiples_of_three = list(range(3, 31, 3))
for number in multiples_of_three:
    print(number)

cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)
for items in cubes:
    print(items)
print(cubes)

# List comprehensions
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)

# Slices
cakes = ['Carrot cake', 'Chocolate cake', 'Banana bread', 'Vanilla cake', 'Sponge cake']
for cake in cakes:
    print(cake)
print('The first three items on the list are:')
for cake in cakes[:3]:
    print(cake)
print('Three items from the middle of the list are:')
for cake in cakes[2:]:
    print(cake)
print('The last three items on the list are:')
for cake in cakes[-3:]:
    print(cake)
friends_pizzas = pizzas[:]
print(friends_pizzas)
print(pizzas)
pizzas.append('Mushroom n chicken')
print(pizzas)
friends_pizzas.append('Beef bacon')
print(friends_pizzas)
print("My favorite pizza's are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizza's are:")
for pizza in friends_pizzas:
    print(pizza)

# Tuples
# Tuples are defined by a comma, the parenthesis make them look neater and more
# readable. If you want to define a tuple with one element you need to include
# a trailing comma.
buffet = ('Steak', 'Rice', 'Chicken', 'Salad', 'Soup')
print('This is what the restaurant offers:')
for meal in buffet:
    print(meal)
buffet = ('Steak', 'Potatoes', 'Pork', 'Salad', 'Soup')
for meal in buffet:
    print(meal)

# If statements
sky = 'Blue'
print("Is sky == 'Blue' ? I predict True.")
print(sky == 'Blue')
print("Is sky == 'grey' ? I predict False")
print(sky == 'grey')
print("Is sky == 'blue' ? I predict False.")
print(sky == 'blue')
print("Is sky.lower() == 'blue' ? I predict True")
print(sky.lower() == 'blue')

age = 18
print(age == 13)
print(age != 18)
print(age > 18)
print(age >= 18)
print(age < 18)
print(age <= 18)
print(age == 18)

weight_one = 76
weight_two = 69
print(weight_two >= 69 and weight_one == 76)
print(weight_one == 76 or weight_two < 68)
print(weight_one == 76 and weight_two < 68)
print(weight_one != 76 and weight_two == 69)

utensils = ['Fork', 'Spoon', 'Plate', 'Cup', 'Knife']
print('Fork' in utensils)
print('Fork' not in utensils)
print('fork' in utensils)
print('fork' not in utensils)
print(len(utensils))

# if-elif-else statements
alien_color = 'yellow'
if alien_color == 'green':
    print('You just earned 5 points')
if alien_color == 'yellow':
    print('You just earned 5 points!')

if alien_color == 'yellow':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')
if alien_color == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')

if alien_color == 'yellow':
    print('You have just earned 5 points!')
elif alien_color == 'green':
    print('You just earned 10 points!')
else:
    print('You have just earned 15 points!')
if alien_color == 'green':
    print('You have just earned 5 points!')
elif alien_color == 'yellow':
    print('You just earned 10 points!')
else:
    print('You have just earned 15 points!')
if alien_color == 'red':
    print('You have just earned 5 points!')
elif alien_color == 'green':
    print('You just earned 10 points!')
else:
    print('You have just earned 15 points!')

age = 23
if age < 2:
    print('You are a baby')
elif 2 <= age <= 4:
    print('You are a toddler')
elif 4 <= age <= 13:
    print('You are a kid')
elif 13 <= age < 20:
    print('You are a teenager')
elif 20 <= age < 65:
    print('You are an adult')
elif age > 65:
    print('You are an elder')

years = int(input("How old are you?: "))
print(f"Hello, you are {years} years old!")
if years < 2:
    print('You are a baby')
elif 2 <= years <= 4:
    print('You are a toddler')
elif 4 <= years <= 13:
    print('You are a kid')
elif 13 <= years < 20:
    print('You are a teenager')
elif 20 <= years < 65:
    print('You are an adult')
elif years > 65:
    print('You are an elder')

favorite_fruits = ['banana', 'apple', 'mango', 'orange']
if 'banana' in favorite_fruits:
    print('You really like bananas!')

usernames = ['shazzy', 'dreezy', 'ace', 'admin', 'chase']
for name in usernames:
    if name == 'admin':
        print(f"Hello {name.title()}, would you like to see a status report?")
    else:
        print(f"Hello {name.title()}, thank you for logging in again")

usernames.clear()
print(len(usernames))
if usernames:
    for name in usernames:
        if name == 'admin':
            print(f"Hello {name.title()}, would you like to see a status report?")
        else:
            print(f"Hello {name.title()}, thank you for logging in again")
else:
    print('We need to find some users!')

current_users = ['cat', 'caterina', 'bobby', 'bob', 'remi', 'remy']
new_users = ['Caterina', 'irina', 'bob', 'iris', 'taylor', 'aang']
for username in new_users:
    if username.lower() in current_users:
        print('You will have to enter a new username')
    else:
        print(f"{username} is available!")

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for ordinal_number in ordinal_numbers:
    if 1 == ordinal_number:
        print(f"{ordinal_number}st")
    elif 2 == ordinal_number:
        print(f"{ordinal_number}nd")
    elif 3 == ordinal_number:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")

# Dictionaries
person1 = {
    'first_name': 'allan',
    'last_name': 'Mwangi',
    'age': 21,
    'city': 'Washington'}
print(person1)

best_numbers = {
    'kate': 7,
    'ace': 2,
    'maggie': 222,
    'lucky': 1,
    'wayne': 9
}
print("My friend's favorite numbers are:")
print(best_numbers['kate'])
print(best_numbers['ace'])
print(best_numbers['maggie'])
print(best_numbers['lucky'])
print(best_numbers['wayne'])
print(best_numbers.keys(), best_numbers.values())

glossary = {
    'lists': 'Lists are mutable',
    'tuples': 'Tuples are immutable',
    'strings': 'Strings are quoted',
    'integers': 'Integers are not quoted',
    'slices': 'Slices are a part of lists'
}
print('The following are some words I have learnt in Python: ')
print('Lists')
print(f"\t{glossary['lists']}\n")
print('Tuples')
print(f"\t{glossary['tuples']}\n")
print('Strings')
print(f"\t{glossary['strings']}\n")
print('Integers')
print(f"\t{glossary['integers']}\n")
print('Slices')
print(f"\t{glossary['slices']}\n")

for keys, values in glossary.items():
    print(f"{keys.title()}\n\t{values}\n")

glossary['dictionaries'] = 'Dictionaries have key value pairs'
glossary['Variable'] = 'A name that stores a value'
glossary['Print'] = 'Displays and output'
glossary['Indentation'] = 'Spacing that shows code blocks'
glossary['Comment'] = 'Notes in your code that python ignores'

print('The following words are words I have learnt in python: ')
for keys, values in glossary.items():
    print(f"{keys.title()}\n\t{values}\n")

rivers = {'nile': 'egypt', 'amazon': 'peru', 'yangtze': 'china'}
for k, v in rivers.items():
    print(f"The {k.title()} river runs through {v.title()}.")

print('These are the rivers in my dictionary: ')
for k in rivers.keys():
    print(f"{k.title()}")

print('These are the countries in my dictionary: ')
for v in rivers.values():
    print(f"{v.title()}")

favorite_langauges = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
students = ['matt', 'jen', 'ben', 'phil']
for student in students:
    if student in favorite_langauges.keys():
        print(f"Thank you {student.title()} for taking the poll.")
    else:
        print(f"{student.title()}, you are invited to take the poll.")

print(person1)
person2 = {
    'first_name': 'milly',
    'last_name': 'millers',
    'age': 24,
    'city': 'Ohio'
}
person3 = {
    'first_name': 'clive',
    'last_name': 'williams',
    'age': 43,
    'city': 'texas'
}
people = [person1, person2, person3]
print(people)
for person in people:
    print(person)

pet1 = {
    'animal': 'dog',
    'owner': 'winter'
}
pet2 = {
    'animal': 'cat',
    'owner': 'nicole'
}
pet3 = {
    'animal': 'rabbit',
    'owner': 'shazzy'
}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(pet)

favorite_places = {
    'patrick': ['Italy', 'Greece', 'France'],
    'evans': ['morocco', 'south africa', 'zanzibar'],
    'juan': ['florida', 'chicago', 'brazil']
}
print(favorite_places)
for boy, places in favorite_places.items():
    print(f"{boy.title()}'s favorite places are:")
    for place in places:
        print(f"{place.title()}")

print(best_numbers)
best_numbers['kate'] = [7, 3, 4]
best_numbers['ace'] = [2, 45, 66]
best_numbers['maggie'] = [222, 666, 888]
best_numbers['lucky'] = [1, 99, 54]
best_numbers['wayne'] = [9, 33, 86]
print(best_numbers)
for friend, lucky_numbers in best_numbers.items():
    print(f"{friend.title()}'s favorite numbers are;")
    for lucky_number in lucky_numbers:
        print(lucky_number)

cities = {
    'rome': {
        'country': 'Italy',
        'language': 'italian',
        'fact': 'They have the best pasta'
    },
    'nairobi': {
        'country': 'Kenya',
        'language': 'kiswahili',
        'fact': 'Only city with a national park'
    },
    'abuja': {
        'country': 'nigeria',
        'language': 'english',
        'fact': 'I have no idea'
    }
}
print(cities)
for city, city_info in cities.items():
    print(f"\nInformation about {city.title()}:")
    country = f"{city_info['country']}"
    language = f"{city_info['language']}"
    fact = f"{city_info['fact']}"
    print(f"\tCountry:{country.title()}")
    print(f"\tLanguage:{language.title()}")
    print(f"\tFact:{fact}")
cities['arusha'] = {
    'country': 'tanzania',
    'language': 'swahili',
    'fact': 'Mt.Meru is found there'
}
print(cities)
for city, city_info in cities.items():
    print(f"\nInformation about{city.title()}:")
    country = f"{city_info['country']}"
    language = f"{city_info['language']}"
    fact = f"{city_info['fact']}"
    print(f"\tCountry: {country.title()}")
    print(f"\tLanguage: {language.title()}")
    print(f"\tFact: {fact.title()}")

# User input and while loops.
rental_car = input("Which type of rental car do you want? ")
print(f"Let me see if I can find you a {rental_car.title()}")

dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)
if dinner_group > 8:
    print("You'll have to wait for another table")
else:
    print("Your table is ready!")

random_number = input("Give me a number: ")
random_number = int(random_number)
if random_number % 10 == 0:
    print(f"{random_number} is a multiple of 10")
else:
    print("Try again!")

prompt = "\nWhich pizza toppings would you like? "
prompt += "\n(Enter 'quit' when done!)\n"
pizza_toppings = True
while pizza_toppings:
    toppings = input(prompt)
    if toppings == 'quit':
        pizza_toppings = False
        print("Great! Your pizza is now in the oven.")
    else:
        print(f"I'll add {toppings.title()} to your pizza!")

# Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.
while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        if age < 3:
            print("The ticket is free!")
            break
        elif 3 <= age <= 12:
            print("The ticket is $10.")
            break
        else:
            print("The ticket is $15.")
            break
    except ValueError:
        print("Enter numeric values.")

# Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value
while True:
    age = input("How old are you?\n(Enter 'quit' when done: ")
    if age == 'quit':
        print("Thank you for your order!")
        break
    try:
        age = int(age)
        if age < 3:
            print("The ticket is free!")
        elif 3 <= age <= 12:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")
    except ValueError:
        print("Enter numeric values.")

# Deli: Make a list called sandwich_orders and fill it with the names of vari-
# ous sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
sandwich_orders = ['cheese sandwich', 'bacon n beef sandwich', 'chicken sandwich', 'beef sandwich']
finished_sandwiches = []
while sandwich_orders:
    cooking_sandwiches = sandwich_orders.pop()
    print(f"I am making your {cooking_sandwiches}.")
    finished_sandwiches.append(cooking_sandwiches)
print("The following sandwiches have been made: ")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} is ready!")

# No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
sandwich_orders = [
    'cheese sandwich',
    'pastrami sandwich',
    'bacon n beef sandwich',
    'pastrami sandwich',
    'chicken sandwich',
    'beef sandwich',
    'pastrami sandwich'
]
finished_sandwiches = []
print(sandwich_orders)
print("\nThe deli has run out of pastrami sandwich.")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
for sandwich in sandwich_orders:
    print("These are the sandwiches")
    print(sandwich.title())

dream_vacation = {}
while True:
    user = input("What is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")
    dream_vacation[user] = vacation
    repeat = input("Would you like someone else to record their dream destination? yes/no : ")
    if repeat == 'no':
        break
for user, vacation in dream_vacation.items():
    print(f"{user.title()}:\n\t{vacation}")
    print()
