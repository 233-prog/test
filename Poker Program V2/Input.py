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

        print(f"Your user cards are: {user_cards}")
        print(f"Board cards: {board_cards}")

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

        print(f"User cards as tuples: {user_cards_tuples}")
        print(f"Board cards as tuples: {board_cards_tuples}")

user_input()

from collections import Counter

card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

# This function checks if a list of ranks is in a sequence, like 5,6,7,8,9.
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

# This function will determine the poker hand from a list of 5 or more cards.
def evaluate_hand(cards):
    # Let's pull out ranks and suits into their own lists.
    rank_list = [card[0] for card in cards]
    suit_list = [card[1] for card in cards]
    
    rank_count = Counter(rank_list)
    suit_count = Counter(suit_list)
    
    # 1) Check for a Straight Flush
    for suit in suit_count:
        if suit_count[suit] >= 5:
            suited_cards = [card for card in cards if card[1] == suit]
            suited_ranks = [card[0] for card in suited_cards]
            
            if is_sequence(suited_ranks):
                j = 0
                highest_card = suited_ranks[j]
                j = j + 1
                while j < len(suited_ranks):
                    if card_value[suited_ranks[j]] > card_value[highest_card]:
                        highest_card = suited_ranks[j]
                    j = j + 1
                return "Straight Flush"
    
    # 2) Check for Four of a Kind (4 cards of the same rank)
    for rank, count in rank_count.items():
        if count == 4:
            return "Four of a Kind"
    
    # 3) Check for a Full House (3 of a kind + a pair)
    three_of_a_kind_rank = None
    pair_rank = None
    for rank, count in rank_count.items():
        if count == 3:
            three_of_a_kind_rank = rank
        elif count == 2:
            pair_rank = rank
    
    if three_of_a_kind_rank is not None and pair_rank is not None:
        return "Full House", three_of_a_kind_rank, pair_rank
    
    # 4) Check for a Flush (5 cards of the same suit)
    for suit_key, suit_count in suit_count.items():
        if suit_count >= 5:
            flush_cards = [card for card in cards if card[1] == suit_key]
            sorted_flush_cards = sorted(flush_cards, key=lambda card: card_value[card[0]], reverse=True)
            top_five = sorted_flush_cards[:5]
            return "Flush", top_five
    
    # 5) Check for a Straight (5 cards in a row, any suits)
    if is_sequence(rank_list):
        k = 0
        highest_straight_card = rank_list[k]
        k = k + 1
        while k < len(rank_list):
            if card_value[rank_list[k]] > card_value[highest_straight_card]:
                highest_straight_card = rank_list[k]
            k = k + 1
        return "Straight"
    
    # 6) Check for Three of a Kind
    for rank, count in rank_count.items():
        if count == 3:
            return "Three of a Kind", rank
    
    # 7) Check for Two Pair
    all_pairs = [rank for rank, count in rank_count.items() if count == 2]
    if len(all_pairs) >= 2:
        sorted_pairs = sorted(all_pairs, key=lambda rank: card_value[rank], reverse=True)
        top_two = sorted_pairs[:2]
        return "Two Pair", top_two
    
    # 8) Check for One Pair
    for rank, count in rank_count.items():
        if count == 2:
            return "One Pair", rank
    
    # 9) If none of those happen, we pick a High Card
    k = 0
    highest_card = rank_list[k]
    k = k + 1
    while k < len(rank_list):
        if card_value[rank_list[k]] > card_value[highest_card]:
            highest_card = rank_list[k]
        k = k + 1
    return "High Card", highest_card

my_result = evaluate_hand()
print(my_result)

