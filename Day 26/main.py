import pandas

ALPHABET_PATH = "Day 26/nato_phonetic_alphabet.csv"
nato = pandas.read_csv(ALPHABET_PATH)
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
word = input("Enter a word: ")
try:
    output = [nato_dict[n.upper()] for n in word]
except KeyError:
    output = "Please use only letters"
print(output)
