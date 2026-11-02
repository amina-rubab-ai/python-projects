import random

LOGO = r"""
 .-------.   .-------.
 | A     |   | K     |
 |   ^   |   |   ^   |
 |  / \  |   |  / \  |
 |  \_/  |   |  \_/  |
 |     A |   |     K |
 '-------'   '-------'
      B L A C K J A C K
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(hand):
    # A hand of exactly two cards that adds up to 21 is a Blackjack (score 0)
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    # If we go over 21 and hold an Ace (11), count that Ace as 1 instead
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, the computer has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "The computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose"


def ask_yes_no(question):
    answer = input(question).lower()
    while answer not in ("y", "n"):
        answer = input("Please type 'y' or 'n': ").lower()
    return answer


def play_game():
    print(LOGO)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            if ask_yes_no("Type 'y' to get another card, type 'n' to pass: ") == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while ask_yes_no("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 3)
    play_game()