import random

DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return random.choice(DECK)


def calculate_score(hand):
    total = sum(hand)

    # Adjust Ace from 11 to 1 if total > 21
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)

    return total


def is_blackjack(hand):
    return len(hand) == 2 and sum(hand) == 21


def show_status(user_hand, dealer_hand):
    print("\nYour cards:", user_hand, "Score:", calculate_score(user_hand))
    print("Dealer first card:", dealer_hand[0])


def compare_scores(user_score, dealer_score, user_hand, dealer_hand):
    if is_blackjack(user_hand) and not is_blackjack(dealer_hand):
        return "Blackjack! You WIN! 🎉"

    if is_blackjack(dealer_hand) and not is_blackjack(user_hand):
        return "Dealer has Blackjack! Dealer WIN!"

    if user_score > 21:
        return "You busted! Dealer WIN!"

    if dealer_score > 21:
        return "Dealer busted! You WIN!"

    if user_score > dealer_score:
        return "You WIN!"

    if dealer_score > user_score:
        return "Dealer WIN!"

    return "It's a DRAW!"


def blackjack_game():
    user_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    show_status(user_hand, dealer_hand)

    # Check instant blackjack
    if is_blackjack(user_hand) or is_blackjack(dealer_hand):
        user_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)
        print("\nFinal Hands:")
        print("Your hand:", user_hand, "Score:", user_score)
        print("Dealer hand:", dealer_hand, "Score:", dealer_score)
        print(compare_scores(user_score, dealer_score, user_hand, dealer_hand))
        return

    # User turn
    while True:
        user_score = calculate_score(user_hand)

        if user_score > 21:
            break

        choice = input("\nType 'y' to draw another card, 'n' to stand: ").lower()

        if choice == 'y':
            new_card = draw_card()
            user_hand.append(new_card)
            print("You drew:", new_card)
            print("Your hand:", user_hand, "Score:", calculate_score(user_hand))
        elif choice == 'n':
            break
        else:
            print("Invalid input! Please type y or n.")

    # Dealer turn
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(draw_card())

    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\n================ FINAL RESULT ================")
    print("Your final hand:", user_hand, "Score:", user_score)
    print("Dealer final hand:", dealer_hand, "Score:", dealer_score)

    print(compare_scores(user_score, dealer_score, user_hand, dealer_hand))


# Main loop
while True:
    start = input("\nDo you want to play Blackjack? (y/n): ").lower()

    if start == 'y':
        blackjack_game()
    elif start == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Please type y or n.")
