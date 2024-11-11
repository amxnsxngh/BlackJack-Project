from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
    user_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)
    return user_cards, computer_cards


def calculate_score(user_cards, computer_cards):
    def check_blackjack(hand):
        if len(hand) == 2 and 11 in hand and 10 in hand:
            return 0
        return sum(hand)

    user_score = check_blackjack(user_cards)
    computer_score = check_blackjack(computer_cards)

    if user_score == 0 or computer_score == 0:
        return user_score, computer_score

    while user_score > 21 and user_cards.count(11) > 0:
        user_cards.remove(11)
        user_cards.append(1)
        user_score = sum(user_cards)

    while computer_score > 21 and computer_cards.count(11) > 0:
        computer_cards.remove(11)
        computer_cards.append(1)
        computer_score = sum(computer_cards)

    return user_score, computer_score


def play_game():
    print(logo)
    user_cards, computer_cards = deal_cards()

    user_score, computer_score = calculate_score(user_cards, computer_cards)

    print(f"User cards: {user_cards}, User score: {user_score}")
    print(f"Computers first card: {computer_cards[0]}")

    if user_score == 0:
        print("User got a Blackjack! User wins!")
        return

    if computer_score == 0:
        print("Computer got a Blackjack! Computer wins!")
        return

    if user_score > 21:
        print("User Loses")
        return

    elif user_score == 21:
        print("User wins with a Blackjack!")

    while user_score < 21:
        continue_game = input("Type 'y' to draw another card, type 'n' to pass: ")
        if continue_game.lower() == 'y':
            user_cards.append(random.choice(cards))
            user_score, computer_score = calculate_score(user_cards, computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"computer's first card: {computer_cards[0]}")
            if user_score > 21:
                print("User loses! Score exceeds 21.")
                return
        elif continue_game.lower() == 'n':
            break

    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        user_score, computer_score = calculate_score(user_cards, computer_cards)
        print(f"Computer's final hand: {computer_cards} | Computer's score: {computer_score}")
        if computer_score > 21:
            print("Computer loses!")
            print("You Win!!!")
            return

    if user_score == computer_score:
        print(f"your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards} | Computer's score: {computer_score}")
        print("DRAW!!!")

    elif user_score > computer_score:
        print(f"your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards} | Computer's score: {computer_score}")
        print("You Win!!!")

    elif user_score < computer_score:
        print(f"your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards} | Computer's score: {computer_score}")
        print("You Lose!!!")


while True:
    game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

    if game.lower() == "y":
        print("\n" * 15)
        play_game()
    else:
        print("Bye Bye")
        break
