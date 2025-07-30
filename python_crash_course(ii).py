# Functions.
# 8-1. Message: Write a function called display_message() that prints one sen-
# tence telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.
def display_message():
    print("I am learning about functions in this chapter! It's about to get real!")


display_message()


# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")


favorite_book('Alice in wonderland')


# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the message to be printed on it is {message}.")


make_shirt(3, "Baddest")
make_shirt(size=5, message='Babe')


# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
def make_shirt(size="large", message="I love python"):
    print(f"The size of the shirt is {size} and the message to be printed on it is'{message}'.")


make_shirt()
make_shirt("medium")
make_shirt("small", "I love functions")


# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
def describe_city(city, country="Kenya"):
    print(f"{city.title()} is in {country.title()}.")


describe_city("nairobi")
describe_city('kisumu')
describe_city('arusha','tanzania')


# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.
def city_country(city, country):
    city_pair = f"{city.title()}, {country.title()}"
    return city_pair


country_pair = city_country("Nairobi", "kenya")
print(country_pair)
country_pair = city_country("Lagos", "nigeria")
print(country_pair)
country_pair = city_country("cairo", "egypt")
print(country_pair)


# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.
def make_album(artist, album):
    album_list = {
        'name': artist.title(),
        'title': album.title()
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


def make_album(artist, album, songs=None):
    album_list = {
        'name': artist.title(),
        'title': album.title()
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
def make_album(artist, album, songs=None):
    album_list = {
        'name': artist.title(),
        'title': album.title()
    }
    if songs:
        album_list['songs'] = songs
    return album_list
