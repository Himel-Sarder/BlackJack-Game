import random

print("================================================")
print("\tWelcome to the blackjack game !")
print("===============================================")
print(
  '''
  .------.            _     _            _    _            _    
  |A_  _ |.          | |   | |          | |  (_)          | |   
  |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
  | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
  |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
  `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
  '''
)
# Define card ranks, suits, and values
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

coins = 50
print("\t\tYou have 50 coins !")

# Define function to create deck of cards
def create_deck():
    deck = []
    for rank in ranks:
        for suit in suits:
            card = (rank, suit)
            deck.append(card)
    return deck

# Define function to deal a card
def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

# Define function to calculate hand value
def calculate_hand_value(hand):
    value = 0
    for card in hand:
        rank = card[0]
        value += values[rank]
    return value

# Define function to display hand
def display_hand(hand):
    for card in hand:
        print(card[0], 'of', card[1])

# Define function to check if hand is a blackjack
def is_blackjack(hand):
    return len(hand) == 2 and calculate_hand_value(hand) == 21

# Define function to check if hand is bust
def is_bust(hand):
    return calculate_hand_value(hand) > 21

# Main function to play the game
def play_blackjack(coins):
    print("================================================")
    print()
    if coins < 10:
        print("Sorry, you don't have enough coins to play!")
        print("=====================================")
        print("\t\t\tGame over!")
        print("=====================================")
        return

    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    print("\nYour hand:")
    display_hand(player_hand)
    print("\nDealer's hand:")
    print(dealer_hand[0][0], 'of', dealer_hand[0][1])

    # Player's turn
    while True:
        choice = input("\nDo you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deal_card(deck))
            print("\nYour hand:")
            display_hand(player_hand)
            if is_blackjack(player_hand):
                print("Congratulations! You have a Blackjack!")
                coins += 10
                break
            elif is_bust(player_hand):
                print()
                print("Sorry, you busted! Dealer wins.")
                coins -= 10
                break
        elif choice == 's':
            break
        else:
            print("Invalid choice! Please enter 'h' or 's'.")

    # Dealer's turn
    if not is_bust(player_hand):
        print("\nDealer's hand:")
        display_hand(dealer_hand)
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
            print("\nDealer hits...")
            display_hand(dealer_hand)
            if is_bust(dealer_hand):
                print()
                print("Dealer busted! You win!")
                coins += 10
                break
        if calculate_hand_value(dealer_hand) <= 21:
            if calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
                print()
                print("You win!")
                coins += 10

            elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
                print()
                print("Dealer wins!")
                coins -= 10
            else:
                print("It's a tie!")
                '''
        else:
            print()
            print("Dealer busted! You win!")
            coins += 10
            '''

    print()
    print(f"Current coins: {coins}")   
    print()
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again == 'yes':
        play_blackjack(coins)
    else:
        print("Thanks for playing!")
        print("=====================================")
        print(f"\t\tFinal coins: {coins}")
        print("=====================================")

# Play the game
play_blackjack(coins)
