import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy level: characters appear in order (letters, then symbols, then numbers)
password = ""

for _ in range(nr_letters):
    password += random.choice(letters)

for _ in range(nr_symbols):
    password += random.choice(symbols)

for _ in range(nr_numbers):
    password += random.choice(numbers)

print(f"Easy level password: {password}")

# Hard level: characters are shuffled randomly
password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

hard_password = "".join(password_list)
print(f"Hard level password: {hard_password}")
