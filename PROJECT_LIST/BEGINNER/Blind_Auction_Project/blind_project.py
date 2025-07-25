import art
print(art.logo)
# TODO-1: Ask the user for input
# name = input("What is your name? : ")
# price = int(input("What is your bid? :$ "))

# bids = {}
# TODO-2: Save data into dictionary {name: price}
# bids[name] = price
# store = {
#     name : price,
# }

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = 0
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with bid amount of ${highest_bid}")
# TODO-3: Whether if new bids need to be added


continue_bidder = True
bids = {}
while continue_bidder:
    name = input("What is your name? : ")
    price = int(input("What is your bid? :$ "))
    bids[name] = price
    next_bider = input("Are there any other bidders ? Type 'yes' or 'no'.\n").lower()
    if next_bider == "yes":
        continue_bidder = True
        print("\n" * 20)
    else:
        continue_bidder = False
        find_highest_bidder(bids)



