from game_data import data
import random
import os


def get_different_to_compare(a):
    b = random.choice(data)
    while b["name"] == a["name"]:
        b = random.choice(data)
    return b


def more_followers(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "A"
    if a["follower_count"] < b["follower_count"]:
        return "B"


def round():
    a = random.choice(data)
    b = get_different_to_compare(a)
    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}")
    print("VS")
    print(f"Against B: {b['name']}, a {b['description']} from {b['country']})")
    if input("Who has more followers? Type 'A' or 'B': ") == more_followers(a, b):
        print("You've guessed!")
        return True
    else:
        return False


os.system("cls")
score = 0
print("Higher Lower Game!")
while round():
    score += 1
    os.system("cls")
    print("Higher Lower Game!")
    print(f"Total Score: {score}")
print(f"You've finished with score: {score}")
