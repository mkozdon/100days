import random


def get_new_deck(number=1):
    return ([10, 10, 10] + [n for n in range(2, 12)]) * 4 * number


def pick_card(deck: list):
    card = random.choice(deck)
    deck.remove(card)
    return card


def evaluate_hand(hand: list):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return sum(hand)


def cpu_turn(hand: list, deck: list):
    print(f"CPU cards: {hand}, current score: {sum(hand)}")
    if sum(hand) == 21:
        print("CPU got Blackjack!")
        return 0
    while sum(hand) < 17:
        hand.append(pick_card(deck))
        current_score = evaluate_hand(hand)
        print(f"CPU cards: {hand}, current score: {current_score}")
    return sum(hand)


def user_turn(hand: list, deck: list):
    if sum(hand) == 21:
        print("You've got Blackjack!")
        return 0
    hit = True
    while hit:
        hit = input("Type 'y' to get another card, 'n' to stand: ") == "y"
        if hit:
            hand.append(pick_card(deck))
            current_score = evaluate_hand(hand)
            print(f"Your cards: {hand}, current score: {current_score}")
            if current_score > 21:
                hit = False
    return sum(hand)


def get_result(user_score, cpu_score):
    if user_score == cpu_score:
        return "Draw!"
    if cpu_score > 21:
        return "You've Won!"
    if user_score == 0:
        return "You've Won!"
    if cpu_score == 0:
        return "You've Lost!"
    if user_score < cpu_score:
        return "You've Lost!"
    elif user_score > cpu_score:
        return "You've Won!"


deck = get_new_deck()
user_hand = [pick_card(deck) for _ in range(0, 2)]
cpu_hand = [pick_card(deck) for _ in range(0, 2)]

print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
print(f"CPU first card: {cpu_hand[0]}\n")
user_score = user_turn(user_hand, deck)
if user_score > 21:
    print("You've Lost!")
else:
    cpu_score = cpu_turn(cpu_hand, deck)
    print(get_result(user_score, cpu_score))
