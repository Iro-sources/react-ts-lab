from clear import clear

bids = {}
bidding_finished = False


# noinspection PyShadowingNames
def find_highest_bidder(bidding_record):
    global bidding_finished
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    def display_winner(winner, highest_bid):
        print(f"The winner is {winner} and they paid {highest_bid}")

    while not bidding_finished:
        name = input("Type your name: ")
        price = int(input("Make a bid: "))
        bids[name] = price
        should_continue = input("Type 'yes' if there is someone else or 'no' if there is not: ")

        if should_continue == 'no':
            bidding_finished = True
            display_winner(winner, highest_bid)
        elif should_continue == 'yes':
            print("done")
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


find_highest_bidder(bids)