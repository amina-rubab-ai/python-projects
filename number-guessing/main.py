import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

LOGO = r"""
  _   _                 _                ____
 | \ | |_   _ _ __ ___ | |__   ___ _ __ / ___|_   _  ___  ___ ___
 |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| |  _| | | |/ _ \/ __/ __|
 | |\  | |_| | | | | | | |_) |  __/ |  | |_| | |_| |  __/\__ \__ \
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   \____|\__,_|\___||___/___/
"""


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while level not in ("easy", "hard"):
        level = input("Please type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    return HARD_LEVEL_ATTEMPTS


def get_guess():
    guess = input("Make a guess: ")
    while not guess.isdigit() or not 1 <= int(guess) <= 100:
        guess = input("Please enter a whole number between 1 and 100: ")
    return int(guess)


def give_hint(guess, answer):
    if guess > answer:
        print("Too high.")
    else:
        print("Too low.")


def game():
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()

    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = get_guess()

        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            return

        give_hint(guess, answer)
        turns -= 1
        if turns > 0:
            print("Guess again.")

    print(f"You've run out of guesses. The number was {answer}. You lose.")


play_again = "y"
while play_again == "y":
    game()
    play_again = input("\nPlay again? Type 'y' or 'n': ").lower()