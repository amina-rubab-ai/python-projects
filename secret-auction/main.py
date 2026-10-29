LOGO = """
=================================
      S E C R E T   A U C T I O N
=================================
"""


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True

print(LOGO)

while continue_bidding:
    name = input("What is your name?: ")

    price = input("What is your bid?: $")
    while not price.isdigit():
        price = input("Please enter a whole number for your bid: $")
    bids[name] = int(price)

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    while should_continue not in ("yes", "no"):
        should_continue = input("Please type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        # Scroll the previous bid off the screen so bids stay secret
        print("\n" * 50)