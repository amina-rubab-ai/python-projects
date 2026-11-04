import random
from art import logo, vs
from data import data


def describe(country):
    return f"{country['name']}, a country in {country['region']}"


def get_choice():
    choice = input("Which country has the higher population? Type 'A' or 'B': ").lower()
    while choice not in ("a", "b"):
        choice = input("Please type 'A' or 'B': ").lower()
    return choice


def is_correct(choice, option_a, option_b):
    if option_a["population"] > option_b["population"]:
        return choice == "a"
    return choice == "b"


def show_populations(option_a, option_b):
    print(f"{option_a['name']}: {option_a['population']} million people")
    print(f"{option_b['name']}: {option_b['population']} million people")


def ask_yes_no(question):
    answer = input(question).lower()
    while answer not in ("y", "n"):
        answer = input("Please type 'y' or 'n': ").lower()
    return answer


def game(high_score):
    """Plays one game and returns the score reached."""
    print(logo)
    score = 0

    # Shuffle once and deal countries one by one so none repeats in a game
    countries = data.copy()
    random.shuffle(countries)
    option_b = countries.pop()

    while countries:
        option_a = option_b
        option_b = countries.pop()

        print(f"Score: {score}   |   High score: {max(score, high_score)}\n")
        print(f"Compare A: {describe(option_a)}.")
        print(vs)
        print(f"Against B: {describe(option_b)}.")

        choice = get_choice()

        print()
        show_populations(option_a, option_b)
        if is_correct(choice, option_a, option_b):
            score += 1
            print(f"You're right! Current score: {score}.\n")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            return score

    print(f"Amazing! You went through every country. Final score: {score}.")
    return score


def main():
    high_score = 0
    play_again = "y"
    while play_again == "y":
        score = game(high_score)
        if score > high_score:
            high_score = score
            print("New high score!")
        play_again = ask_yes_no("\nPlay again? Type 'y' or 'n': ")
    print(f"Thanks for playing. Your high score: {high_score}.")


if __name__ == "__main__":
    main()