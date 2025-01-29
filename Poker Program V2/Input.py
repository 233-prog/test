def is_valid_card(card, valid_ranks, valid_suits):
    card_length = len(card)
    if card_length != 2:
        return False
    first_char = card[0]
    second_char = card[1]
    if first_char not in valid_ranks:
        return False
    if second_char not in valid_suits:
        return False
    return True

def check_duplicates(cards_list):
    return len(cards_list) != len(set(cards_list))

def cards_input(cards_type, valid_counts):
    valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    valid_suits = ["S", "H", "D", "C"]

    while True:
        cards_input = input(f"Enter the {cards_type} cards: ").strip()
        cards_list = cards_input.split()

        if len(cards_list) not in valid_counts:  
            print("Invalid format pls recheck.")
            continue

        if check_duplicates(cards_list):
            print("Duplicate cards detected. Please enter unique cards.")
            continue

        valid_cards = True
        for card in cards_list:
            if not is_valid_card(card, valid_ranks, valid_suits):
                valid_cards = False
                print("Invalid card detected. Please enter cards in the correct format (XY XY).")
                break
        
        if valid_cards:
            return cards_list

def user_input():
    while True:
        user_cards = cards_input("user", [2])  
        board_cards = cards_input("board", [0, 3, 4, 5])  

        combined_cards = user_cards + board_cards
        if check_duplicates(combined_cards):
            print("Duplicate cards detected. Please enter unique cards.")
            continue  

        user_cards_tuples = []
        for card in user_cards:
            rank = card[0]
            suit = card[1]
            user_cards_tuples.append((rank, suit))

        board_cards_tuples = []
        for card in board_cards:
            rank = card[0]
            suit = card[1]
            board_cards_tuples.append((rank, suit))
        return user_cards_tuples, board_cards_tuples     
     
user_cards_tuples, board_cards_tuples = user_input()
print(f"User cards as tuples: {user_cards_tuples}")
print(f"Board cards as tuples: {board_cards_tuples}")
