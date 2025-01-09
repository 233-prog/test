def user_input():
    valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    valid_suits = ["S", "H", "D", "C"]

    # Function to validate a card
    def is_valid_card(card):
        if len(card) < 2:
            return False
        rank, suit = card[:-1], card[-1]
        return rank in valid_ranks and suit in valid_suits

    # Prompt user for two player cards
    while True:
        player_cards = input("Enter your two cards (e.g., '10H KD'): ").split()
        if len(player_cards) != 2 or not all(is_valid_card(card) for card in player_cards):
            print("Invalid input. Please enter exactly two valid cards.")
        else:
            break

    # Prompt user for the number of board cards
    while True:
        try:
            num_board_cards = int(input("Enter the number of board cards (0, 3, 4, or 5): "))
            if num_board_cards in [0, 3, 4, 5]:
                break
            else:
                print("Invalid number of board cards. Please enter 0, 3, 4, or 5.")
        except ValueError:
            print("Please enter a valid number.")

    # If board cards are required, prompt for them
    board_cards = []
    if num_board_cards > 0:
        print(f"Enter {num_board_cards} board cards:")
        while len(board_cards) < num_board_cards:
            card = input(f"Enter card {len(board_cards) + 1}: ")
            if is_valid_card(card):
                board_cards.append(card)
            else:
                print("Invalid card. Please try again.")

    # Print collected information
    print("\n--- Collected Information ---")
    print(f"Player Cards: {player_cards}")
    print(f"Number of Board Cards: {num_board_cards}")
    if num_board_cards > 0:
        print(f"Board Cards: {board_cards}")

    return player_cards, board_cards, num_board_cards

# Example usage
user_input()
