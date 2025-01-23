def cards_input(cards_type, expected_count):
    valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    valid_suits = ["S", "H", "D", "C"]

    while True:
        cards_input = input(f"Enter the {cards_type} cards: ").strip()
        cards_list = cards_input.split()

        if len(cards_list) != expected_count:  
            print(f"Please enter {expected_count} cards.")
            continue
        
        valid_cards = True
        
        for card in cards_list:
            card_length = len(card)
            if card_length != 2:
                valid_cards = False
            first_char = card[0]
            second_char = card[1]

            if first_char not in valid_ranks:
                valid_cards = False
            if second_char not in valid_suits:
                valid_cards = False

            if not valid_cards:
                print("Invalid card detected. Please enter cards in the correct format (XY XY).")
                break
        
        if valid_cards:
            return cards_list

def get_board_cards():
    valid_board_numbers = [0, 3, 4, 5]
    board_count_input = input("How many community cards do you want to enter (0, 3, 4, 5)? ").strip()

    board_count_valid = board_count_input.isdigit()
    board_count_value = int(board_count_input)  

    while board_count_value not in valid_board_numbers:
        if not board_count_valid:
            print("Invalid input. Please enter a number.")
        else:
            print("Invalid number of community cards. Valid options are: 0, 3, 4, 5.")
        board_count_input = input("How many community cards do you want to enter (0, 3, 4, 5)? ").strip()

    board_count = int(board_count_input)
    
    if board_count > 0:
        board_cards = cards_input("board", board_count) 
    else:
        board_cards = []

    return board_cards

def user_input():
    user_cards = cards_input("user", 2)  
    
    board_cards = get_board_cards()
    
    print(f"Your user cards are: {user_cards}")
    print(f"Board cards: {board_cards}")

user_input()
