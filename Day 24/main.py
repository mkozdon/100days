# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"
INPUT_NAMES = "Day 24/Input/Names/invited_names.txt"
STARTING_LETTER = "Day 24/Input/Letters/starting_letter.txt"


def save_mail(body: str, name: str):
    with open(f"Day 24/Output/ReadyToSend/letter_for_{name}.txt", "w") as output:
        output.write(body.replace(PLACEHOLDER, name))


with open(STARTING_LETTER, "r") as letter_file:
    letter = letter_file.read()

with open(INPUT_NAMES, "r") as names_file:
    for name in names_file:
        save_mail(letter, name.rstrip())
