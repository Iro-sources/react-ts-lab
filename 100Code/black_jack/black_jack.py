import random


#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    return sum(cards)
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
# and return 0 instead of the actual score. 0 will represent a blackjack in our game.