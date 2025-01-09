valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
valid_suits = ["S", "H", "D", "C"]

def validate_input(input_value, valid_values):
    return input_value in valid_values

def validate_overall_input(player_cards, com_cards, num_com_cards):
    
    for card in player_cards:
        rank, suit = card
        if not validate_input(rank, valid_ranks) or not validate_input(suit, valid_suits):
            return "Invalid card value in player cards."

    for card in com_cards:
        rank, suit = card
        if not validate_input(rank, valid_ranks) or not validate_input(suit, valid_suits):
            return "Invalid card value in community cards."

    if num_com_cards not in [0, 3, 4, 5]:
        return "Invalid number of community cards."

    return "Valid input."

def is_valid_card(card, valid_ranks, valid_suits):
    if len(card) < 2:  
        return False
    rank, suit = card
    return validate_input(rank, valid_ranks) and validate_input(suit, valid_suits)

def user_input():
    while True:
        player_cards = input("Enter your two cards: ").split()
        if len(player_cards) != 2 or not all(is_valid_card(card, valid_ranks, valid_suits) for card in player_cards):
            print("Invalid input. Please enter exactly two valid cards.")
        else:
            break

    while True:
        try:
            num_com_cards = int(input("Enter the number of community cards: "))
            if num_com_cards in [0, 3, 4, 5]:
                break
            else:
                print("Invalid number of community cards. Please enter 0, 3, 4, or 5.")
        except ValueError:
            print("Please enter a valid number.")

    com_cards = []
    if num_com_cards > 0:
        print(f"Enter {num_com_cards} community cards:")
        while len(com_cards) < num_com_cards:
            card = input(f"Enter card {len(com_cards) + 1}: ")
            if is_valid_card(card, valid_ranks, valid_suits):
                com_cards.append(card)
            else:
                print("Invalid card. Please try again.")

    validation_result = validate_overall_input(player_cards, com_cards, num_com_cards)
    if validation_result != "Valid input.":
        print(validation_result)
        return user_input()  
    
    print(f"Player Cards: {player_cards}")
    print(f"Number of Community Cards: {num_com_cards}")
    if num_com_cards > 0:
        print(f"Community Cards: {com_cards}")

    return player_cards, com_cards, num_com_cards

user_input()
