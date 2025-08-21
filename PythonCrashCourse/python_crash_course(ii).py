# Functions.
def display_message():
    """
    Prints one sentence telling everyone what I am learning
    :return:
    """
    print("I am learning about functions in this chapter! It's about to get real!")


display_message()


def favorite_book(title):
    """
    This function prints the users favorite books
    :param title:
    :return:
    """
    print(f"One of my favorite books is {title.title()}")


favorite_book('Alice in wonderland')


def make_shirt(size, message):
    """
    This function summaries the size of the shirt and the message printed on it.
    :param size:
    :param message:
    :return:
    """
    print(f"The size of the shirt is {size} and the message to be printed on it is {message}.")


make_shirt(3, "Baddest")
make_shirt(size=5, message='Babe')


def make_shirt(size="large", message="I love python"):
    """
    This function summarizes the size of the shirt and the message printed on it.
    :param size:
    :param message:
    :return:
    """
    print(f"The size of the shirt is {size} and the message to be printed on it is'{message}'.")


make_shirt()
make_shirt("medium")
make_shirt("small", "I love functions")


def describe_city(city, country="Kenya"):
    """
    This function summarizes the information about a city.
    :param city:
    :param country:
    :return:
    """
    print(f"{city.title()} is in {country.title()}.")


describe_city("nairobi")
describe_city('kisumu')
describe_city('arusha', 'tanzania')


def city_country(city, country):
    """
    This function shows the city, alongside the country
    :param city:
    :param country:
    :return:
    """
    city_pair = f"{city.title()}, {country.title()}"
    return city_pair


country_pair = city_country("Nairobi", "kenya")
print(country_pair)
country_pair = city_country("Lagos", "nigeria")
print(country_pair)
country_pair = city_country("cairo", "egypt")
print(country_pair)


def make_album(artist, albumm):
    """
    This function takes in the data about an artist and stores it in a dict
    :param artist:
    :param albumm:
    :return:
    """
    album_list = {
        'name': artist.title(),
        'title': albumm.title()
    }
    return album_list


albums = make_album('victony', 'stubborn')
for name, album in albums.items():
    print(f"{name.upper()}:\n\t{album}")
print(albums)
albums = make_album('davido', 'five')
print(albums)
albums = make_album('odumodu', 'the machine')
print(albums)


def make_album(artist, albumm, songs=None):
    """
    This function takes in the data about an artist and stores it in a dict
    :param artist:
    :param albumm:
    :param songs:
    :return:
    """
    album_list = {
        'name': artist.title(),
        'title': albumm.title()
    }
    if songs:
        album_list['songs'] = songs
    return album_list


albums = make_album('burna boy', 'no signs of weakness', 16)
print(albums)
albums = make_album('bnxn', 'captain')
print(albums)


# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.
def make_album(artist, albumm, songs=None):
    """
    This function takes in the data about an artist and stores it in a dict
    :param artist:
    :param albumm:
    :param songs:
    :return:
    """
    album_list = {
        'name': artist.title(),
        'title': albumm.title()
    }
    if songs:
        album_list['songs'] = songs
    return album_list


while True:
    print("Type 'q' when done")
    artist_name = input("What is the name of the artist? ")
    if artist_name == 'q':
        break
    album_title = input("What is the name of the album? ")
    if album_title == 'q':
        break
    combined_input = make_album(artist_name, album_title)
    print(combined_input)

short_messages = ['Hellooo', 'goodbye', 'good morning', 'good evening', 'goodnight']


def show_messages(messages):
    """
    This function prints each text message
    :param messages:
    :return:
    """
    print("These are some short messages you can send:")
    for message in messages:
        print(f"{message.title()}!")


show_messages(short_messages)
sent_messages = []


def send_messages(short_messages, sent_messages):
    """
    This function sends text messages from the short message list and moves each message to a new list.
    :param sent_messages:
    :param short_messages:
    :return:
    """
    while short_messages:
        current_message = short_messages.pop()
        print(f"Sending this message: {current_message.title()}!")
        sent_messages.append(current_message)


send_messages(short_messages[:], sent_messages)
print(short_messages)
print(sent_messages)


# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sandwich
# that’s being ordered. Call the function three times, using a different number of arguments each time.
def toppings(*args):
    """
    This function prints the toppings a user wants in a sandwich
    :param args:
    :return:
    """
    print(f"Your pizza has the following topping(s):")
    for topping in args:
        print(f"\t{topping}")


toppings('pepperoni')
toppings('cheese', 'beef', 'ham')
toppings('cheese', 'pork', 'ham', 'bacon', 'bbq')


# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
# profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.
def build_profile(first, last, **user_info):
    """
    Build a dict, containing everything we know about a user
    :param first:
    :param last:
    :param user_info:
    :return:
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Sharon', 'Wanjiru', age=22, location='kikuyu', field='data')
print(user_profile)


# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly.
def car_details(manufacturer, model, **kwargs):
    """
    This function stores data about cars in a dict
    :param manufacturer:
    :param model:
    :param kwargs:
    :return:
    """
    kwargs['Manufacturer'] = manufacturer
    kwargs['Model'] = model
    return kwargs


car_info = car_details('mazda', 'cx5', color='pink', tow_package=True)
print(car_info)


# Classes
# 9-1. Restaurant: Make a class called Restaurant. The _init_() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"This restaurant is called {self.name}")
        print(f"The cuisine type is {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is open!")


restaurant = Restaurant('For you', 'Chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

my_restaurant = Restaurant('Zen Garden', 'Asian')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant('Big Fish', 'Kenyan')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()


# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.name = self.first_name + ' ' + self.last_name

    def describe_user(self):
        """
        Prints a summary of the user's information
        :return: User information
        """
        print("This is the information we have about the user:")
        print(f"First name: {self.first_name}\n"
              f"Last name: {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Location: {self.location}")

    def greet_user(self):
        """
        Prints a personalized greeting to the user
        :return: Personalized greeting
        """
        print(f"Hello {self.name}!")


user1 = User('Sharon', 'Wanjiru', 20, 'Cairo')
user1.describe_user()
user1.greet_user()
user2 = User('Mike', 'Smith', 18, 'Chicago')
user2.describe_user()
user2.greet_user()
user3 = User('Blue', 'Ivy', 14, 'LA')
user3.describe_user()
user3.greet_user()


# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any nummber
# you like that could represent how many customers were served in, say, a day of business.
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant is called {self.name}")
        print(f"The cuisine type is {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is open!")


restaurant1 = Restaurant('orca', 'swahili')
print(restaurant1.number_served)
restaurant1.number_served = 24
print(restaurant1.number_served)


class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant is called {self.name}")
        print(f"The cuisine type is {self.cuisine}")

    def set_number_served(self, number):
        self.number_served = number

    def open_restaurant(self):
        print(f"{self.name} is open!")


restaurant2 = Restaurant('meko','african')
restaurant2.set_number_served(34)
print(restaurant2.number_served)


class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant is called {self.name}")
        print(f"The cuisine type is {self.cuisine}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increase):
        self.number_served += increase

    def open_restaurant(self):
        print(f"{self.name} is open!")


restaurant4 = Restaurant('sonford', 'english')
restaurant4.set_number_served(10)
restaurant4.increment_number_served(50)
print(restaurant4.number_served)


# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login
# _attempts() that increments the value of login_attempts by 1. Write another
# method called reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.name = self.first_name + ' ' + self.last_name
        self.login_attempts = 0

    def describe_user(self):
        """
        Prints a summary of the user's information
        :return: User information
        """
        print("This is the information we have about the user:")
        print(f"First name: {self.first_name}\n"
              f"Last name: {self.last_name}\n"
              f"Age: {self.age}\n"
              f"Location: {self.location}")

    def greet_user(self):
        """
        Prints a personalized greeting to the user
        :return: Personalized greeting
        """
        print(f"Hello {self.name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

