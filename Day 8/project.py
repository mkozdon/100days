def shift_char(char, shift):
    if ord(char.lower()) < ord("a") or ord(char.lower()) > ord("z"):
        return char
    new_ascii = ord(char.lower()) + shift
    if new_ascii > ord("z"):
        new_ascii -= ord("z") - ord("a") + 1
    elif new_ascii < ord("a"):
        new_ascii += ord("z") - ord("a") + 1
    return chr(new_ascii)


def cipher(text, shift):
    return "".join([shift_char(n, shift) for n in text])


quit = False

while not quit:
    mode = input("Type 'encode' or 'decode':\n")
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    if mode == "encode":
        print(cipher(message, shift))
    elif mode == "decode":
        print(cipher(message, -shift))
    else:
        print("Unknown command.")
    quit = input("type 'yes' if you want to go again. Otherwise type 'no'.\n") == "no"
