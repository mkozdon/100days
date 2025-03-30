import os

bids = {}
get_bidders = True


def get_bidder_name(bids):
    name = input("What is your name?: ")
    while name in bids:
        if input("This name is already used. Try again? 'y'/'n': ") == "y":
            name = input("What is your name?: ")
    return name


def get_bid(bids):
    name = get_bidder_name(bids)
    if name != "":
        bids[name] = int(input("what is your bid?: $"))


print("Welcome to secret auction program.")
while get_bidders:
    get_bid(bids)
    if input("Are there other bidders? Type 'yes' or 'no'.\n") == "no":
        get_bidders = False
    os.system("cls")
max_bid = 0
winner = ""
for bidder in bids:
    if bids[bidder] > max_bid:
        max_bid = bids[bidder]
        winner = bidder

print(f"Auction won by {winner} with ${max_bid}")

# other_bidders = input("Are there other bidders? Type 'yes' or 'no'.\n")
