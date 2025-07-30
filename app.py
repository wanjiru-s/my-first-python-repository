# Exercise 1. Print numbers from 10 to 15 using a while loop.
counter = 10
while counter <= 15:
    print(counter)
    counter += 1
# Exercise 2. Write a while loop that prints numbers from 20 down to 10.
counter = 20
while counter >= 10:
    print(counter)
    counter -= 1

# Exercise 3. Write a while loop that prints numbers from 1 to 10, but stops if the number is 7.
counter = 1
while counter <= 10:
    if counter == 7:
        break
    print(counter)
    counter += 1

# Exercise 4. Write a while loop that prints numbers from 1 to 7, but skips number 4.
counter = 1
while counter <= 7:
    if counter == 4:
        counter += 1
        continue
    print(counter)
    counter += 1

# Exercise 5. Write a while loop that prints "Learning Python!" three times using a boolean variable.
learning = True
counter = 1
while learning:
    print("Learning Python!")
    if counter >= 3:
        learning = False
    counter += 1

# Exercise 6. Write a while loop that prints your name 5 times.
name = "Sharon"
counter = 1
while counter <= 5:
    print(name)
    counter += 1
name = True
counter = 1
while name:
    print("Josh")
    if counter >= 5:
        name = False
    counter += 1

# Exercise 7. Write a while loop that sums numbers from 1 to 10 and prints the final result.
total = 0
counter = 1
while counter <= 10:
    total += counter
    counter += 1
print(total)

# Exercise 8. Write a while loop that asks the user to type "Python" to continue.
language = ""
while language.lower() != 'python':
    language = (input("Which programming language are you studying? "))

# Exercise 9. Write a while loop to print all your 3 favorite movies.
favorite_movie = ['superman', 'smurfs', 'croods']
i = 0
while i < len(favorite_movie):
    print(favorite_movie[i])
    i += 1

# Exercise 10. Create a multiplication table for numbers 1 to 3 using nested while loops.
