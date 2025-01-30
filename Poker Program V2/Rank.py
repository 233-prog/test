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

from collections import Counter

card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10,"J": 11, "Q": 12, "K": 13, "A": 14}

def is_sequence(ranks):
    rank_values_list = [card_value[rank] for rank in ranks]
    sorted_rank_values = sorted(rank_values_list)
    
    j = 0
    while j < len(sorted_rank_values) - 1:
        next_value = sorted_rank_values[j] + 1
        if next_value != sorted_rank_values[j + 1]:
            return False
        j = j + 1
    return True

def evaluate_hand(cards):
    rank_list = []
    for card in cards:
        rank_list.append(card[0])

    suit_list = []
    for card in cards:
        suit_list.append(card[1])
        
    rank_count = Counter(rank_list)
    suit_count = Counter(suit_list)

    #Straight Flush
    
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

    
    #Flush
    for suit_key, suit_count in suit_count.items():
        if suit_count >= 5:
            return "Flush",suit_key
    
    #Straight
    if is_sequence(rank_list):    
        return "Straight"
    
    #Three of a Kind
    for rank, count in rank_count.items():
        if count == 3:
            return "Three of a Kind", rank
    
    #Two Pair
    all_pairs = [rank for rank, count in rank_count.items() if count == 2]
    if len(all_pairs) >= 2:
        return "Two Pair"
    
    #One Pair
    for rank, count in rank_count.items():
        if count == 2:
            return "One Pair", rank

    return "High Card", rank_list[0]  

hand_result = evaluate_hand(user_cards_tuples + board_cards_tuples)
print(f"The hand formed is: {hand_result}")
