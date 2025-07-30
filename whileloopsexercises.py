# Beginner-level real life exercises.
# 1. Flower Quantity Checker
# 💐 Ask the user how many roses they want.
# If the number is less than 1, keep asking.
# Once valid, print: "Order received for X roses!"
# 💡 Real-life use: Prevent users from ordering 0 or negative quantities on your flower site.
shopping = True
while shopping:
    order = int(input("How many roses do you want? "))
    if order <= 0:
        print(order)
    else:
        print(f"Order received for {order} roses!")
        shopping = False
# Revised solution to 1.
# ⚠️ Improvements:
# Don’t use raw int(input()) without validation — it can crash if the user enters non-numeric input.
# shopping = True is okay, but using while True: and break is cleaner in most pro code.
# Avoid printing the invalid number (just re-prompt).
while True:
    order = input("How many roses do you want? ")
    try:
        order = int(order)
        if order > 0:
            print(f"Order received for {order} roses!")
            break
        else:
            print("Enter a number more than zero!")
    except ValueError:
        print("Enter an integer")

# 2. PIN Validation (Login Simulation)
# 🧾 Let the user try to enter the correct PIN (e.g. "4321").
# Keep asking until they get it right.
# Then say: "Access granted!"
password_checking = True
while password_checking:
    pin = int(input("Enter PIN: "))
    if pin != 1234:
        print(pin)
    else:
        print("Access granted!")
        password_checking = False
# Revised solution to 2.
# ⚠️ Improvements:
# Same: int(input()) without handling non-numeric input can crash.
# Avoid printing the wrong PIN — it's a security risk.
correct_pin = 1234
while True:
    pin = input("Enter the pin: ")
    try:
        pin = int(pin)
        if pin == correct_pin:
            print("Access granted!")
            break
        else:
            print("Try again!")
    except ValueError:
        print("Enter numerical digits only!")

# 3. Ask for a Multiple of 10
# 🔢 Keep asking the user for a number until they enter a multiple of 10.
# Use % operator for checking.
# When correct, print: "Thanks!"
multiples = True
while multiples:
    number = int(input("Enter a number: "))
    if number % 10 != 0:
        print(number)
    else:
        print("Thanks!")
        multiples = False
# Revised solution to 3.
# ⚠️ Improvements:
# Again, consider using try/except for safe input.
# No need to store multiples = True—while True is clearer
while True:
    try:
        number = int(input("Please enter a multiple of 10: "))
        if number % 10 == 0:
            print("Thanks!")
            break
        else:
            print("Try again!")
    except ValueError:
        print("Enter numeric values")

# 4. Countdown Timer
# ⏳ Start with a number (e.g. 10) and count down to 0.
# Print each number
# At 0, print: "Time's up!"
count = 10
while count >= 0:
    print(count)
    if count == 0:
        print("Time's up!")
    count -= 1
# Revised solution to 4.
# ⚠️ Optional Tip:
# You can remove the if count == 0 block and handle after loop.
count = 10
while count >= 0:
    print(count)
    count -= 1
print("Time's up!")

# Intermediate-Level Real-Life Exercises
# 5. Phone Number Validator
# 📱 Keep asking for a Kenyan phone number until:
# Starts with "07"
# Exactly 10 digits
# Use .startswith() and len().
contact = True
while contact:
    number = input("Insert Kenyan Phone number: ")
    if number.startswith("07") and len(number) == 10:
        print("You have entered the right number!")
        contact = False
    else:
        print(number)
# Revised solution to 5.
# ⚠️ Improvements:
# You should avoid printing the invalid number.
# Consider checking if it’s all digits using .isdigit().
# Again, while True + break is neater for this case.
while True:
    contact = input("Enter your Kenyan number: ")
    if contact.startswith("07") and len(contact) == 10 and contact.isdigit():
        print("You have entered the right number!")
        break
    else:
        print("Enter a 10 digit number that starts with 07")

# 6. Flower Sales Tracker
# 🧮 Keep asking for sale amounts:
# Add each to a total
# Stop when user types "done"
# Show the total sales
total = 0
tracking = True
while tracking:
    sales = input("How many sales did you make ?\n(Type 'done' when you finish): ")
    if sales.lower() == 'done':
        print("Finished recording sales!")
        tracking = False
        break
    try:
        number = int(sales)
        total += number
    except ValueError:
        print("Enter a number")
print(f"Your total sales are {total}")

# 7. Mini Password Strength Checker
# 🔐 Ask user to create a password.
# Must have at least 8 characters
# Must contain a number
# Loop until it’s strong.
while True:
    password = input("Create a password.")
