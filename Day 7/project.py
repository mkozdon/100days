import random

word_list = ["aardvark", "baboon", "camel"]
word_to_guess = random.choice(word_list).lower()
guessed_letters = []

game_loop = True
health = 6


def get_current_state(word, letters):
    return "".join([n if n in letters else "_" for n in word])


while game_loop:
    current_guess = input("Guess a letter:").lower()
    if current_guess in word_to_guess:
        if current_guess in guessed_letters:
            print("You've already tried this letter.")
            continue
        guessed_letters.append(current_guess)
        current_state = get_current_state(word_to_guess, guessed_letters)
        print(current_state)
        if current_state == word_to_guess:
            print("Good Job!")
            game_loop = False
    else:
        health -= 1
        print(f"This letter is not in the word.\nHealth: {health}/6")
        if health == 0:
            print("You Loose!")
            game_loop = False
