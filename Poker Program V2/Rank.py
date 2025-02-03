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

card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10,"J": 11, "Q": 12, "K": 13, "A": 14}

def is_sequence(ranks):
    rank_values_list = []
    for rank in ranks:
        rank_values_list.append(card_value[rank])
    
    rank_values_list.sort()

    for i in range(len(rank_values_list) - 1):
        current_value = rank_values_list[i]
        next_value = rank_values_list[i + 1]
        expected_next_value = current_value + 1
        if next_value != expected_next_value:
            return False
    
    return True

def count_elements(elements):
    count_dict = {}
    for element in elements:
        if element in count_dict:
            count_dict[element] = count_dict[element] + 1
        else:
            count_dict[element] = 1
    return count_dict

def evaluate_hand(cards):
    rank_list = []
    for card in cards:
        rank_list.append(card[0])

    suit_list = []
    for card in cards:
        suit_list.append(card[1])
        
    rank_count = count_elements(rank_list)
    suit_count = count_elements(suit_list)

    #Straight Flush
    for suit, count in suit_count.items():
        if count >= 5:
            suited_cards = []
            for card in cards:
                if card[1] == suit:
                    suited_cards.append(card)
            suited_ranks = []
            for card in suited_cards:
                suited_ranks.append(card[0])
            if is_sequence(suited_ranks):
                return "Straight Flush", suit

    #Four of a Kind
    for rank, count in rank_count.items():
        if count == 4:
            four_of_a_kind = "Four of a Kind"
            return four_of_a_kind, rank
    
    #Full House
    three_of_a_kind_rank = None
    pair_rank = None
    for rank, count in rank_count.items():
        if count == 3:
            three_of_a_kind_rank = rank
        elif count == 2:
            pair_rank = rank
    
    if three_of_a_kind_rank and pair_rank:
        return "Full House", three_of_a_kind_rank, pair_rank

    
    # Flush
    for suit, count in suit_count.items():
        if count >= 5:
            return "Flush", suit

    # Straight
    rank_values = []
    for rank in rank_list:
        rank_values.append(card_value[rank])
    if is_sequence(rank_values):
        return "Straight"
    
    #Three of a Kind
    for rank, count in rank_count.items():
        if count == 3:
            return "Three of a Kind", rank
    
    #Two Pair
    all_pairs = []
    for rank, count in rank_count.items():
        if count == 2:
            all_pairs.append(rank)
    if len(all_pairs) >= 2:
        return "Two Pair", all_pairs

    #One Pair
    for rank, count in rank_count.items():
        if count == 2:
            return "One Pair", rank

    # High card
    rank_values_sorted = []
    for rank in rank_list:
        rank_value = card_value[rank]
        rank_values_sorted.append(rank_value)
    rank_values_sorted.sort(reverse=True)
    highest_value = max(rank_values_sorted)
    high_card_index = rank_values_sorted.index(highest_value)
    high_card = rank_list[high_card_index]
    print("High Card:", high_card)

hand_result = evaluate_hand(user_cards_tuples + board_cards_tuples)
print(f"The hand formed is: {hand_result}")
