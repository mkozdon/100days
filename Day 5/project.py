import random

letters = [chr(n) for n in range(65, 91)] + [chr(n) for n in range(97, 123)]
numbers = [chr(n) for n in range(48, 58)]
symbols = [chr(n) for n in range(33, 48)]

print("Welcome to password generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

raw_pwd = []
raw_pwd += [random.choice(letters) for n in range(1, nr_letters + 1)]
raw_pwd += [random.choice(symbols) for n in range(1, nr_symbols + 1)]
raw_pwd += [random.choice(numbers) for n in range(1, nr_numbers + 1)]

random.shuffle(raw_pwd)
print("".join(raw_pwd))
