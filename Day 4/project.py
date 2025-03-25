import random

print("What do you choose?")
user_sign = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors."))
cpu_sign = random.choice([user_sign - 1, user_sign, user_sign + 1])
print(cpu_sign)
if user_sign == cpu_sign:
    print("Draw!")
if user_sign < cpu_sign:
    print("Lost!")
if user_sign > cpu_sign:
    print("Win!")
