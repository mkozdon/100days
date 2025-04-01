import random


def get_num_of_guesses():
    difficulty = input("Choose as difficulty. Type 'easy' or 'hard':")
    if difficulty == "easy":
        return 10
    else:
        return 5


def make_guess(attempts, number):
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        return True
    if guess < number:
        print("Too low.")
    if guess > number:
        print("Too high.")
    return False


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


attempts = get_num_of_guesses()
number = random.randrange(1, 101)
guessed = False
while attempts > 0 and not guessed:
    guessed = make_guess(attempts, number)
    attempts -= 1
if attempts <= 0:
    print("Game Over")
