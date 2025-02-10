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

def is_flush(cards, suit_count):
    for suit in suit_count:
        if suit_count[suit] >= 5:
            flush_cards = [card for card in cards if card[1] == suit] 
            flush_cards.sort(key=card_rank_descending)  
            highest_five = flush_cards[:5]
            return "Flush", highest_five
    return None

def card_rank(card):
    return card[0]  

def card_rank_descending(card):
    ranks_order = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    return -ranks_order[card[0]]  

def get_highest_five(cards):
    return cards[:5]

def is_straight(cards):
    if len(cards) >= 5:
        cards.sort(key=card_rank_descending)  
        if is_straight_sequence(cards):
            sequence = get_highest_five(cards)
            return "Straight", sequence
    return None

def is_straight_sequence(cards):
    for i in range(len(cards) - 4):
        if cards[i][0] - cards[i + 4][0] == 4:  
            return True
    return False

def straight_flush(cards, suit_count):
    for suit in suit_count:
        if suit_count[suit] >= 5:
            suited_cards = [card for card in cards if card[1] == suit]  
            if is_straight(suited_cards):
                sequence = get_highest_five(suited_cards)
                return "Straight Flush", sequence
    return None

def four_of_a_kind(rank_count):
    for rank in rank_count:
        if rank_count[rank] == 4:
            return "Four of a Kind", rank
    return None

def full_house(rank_count):
    three_list = []
    pair_list = []
    for rank in rank_count:
        if rank_count[rank] == 3:
            three_list.append(rank)
        elif rank_count[rank] >= 2:
            pair_list.append(rank)
    
    if len(three_list) >= 2:
        three_list.sort(reverse=True)
        trips = three_list[0]
        pair = three_list[1]
        return "Full House", trips, pair
    elif len(three_list) == 1 and len(pair_list) >= 1:
        trips = three_list[0]
        pair_list.sort(reverse=True)
        pair = pair_list[0]
        return "Full House", trips, pair
    return None

def flush(cards, suit_count):
    return is_flush(cards, suit_count)

def straight(cards):
    return is_straight(cards)

def three_of_a_kind(rank_count):
    three_kind_ranks = []
    for rank in rank_count:
        if rank_count[rank] == 3:
            three_kind_ranks.append(rank)
    if len(three_kind_ranks) > 0:
        three_kind_ranks.sort(reverse=True)
        highest_three = three_kind_ranks[0]
        return "Three of a Kind", highest_three
    return None

def two_pair(rank_count):
    pair_ranks = []
    for rank in rank_count:
        if rank_count[rank] == 2:
            pair_ranks.append(rank)
    if len(pair_ranks) >= 2:
        pair_ranks.sort(reverse=True)
        highest_pair = pair_ranks[0]
        second_highest_pair = pair_ranks[1]
        return "Two Pair", highest_pair, second_highest_pair
    return None

def one_pair(rank_count):
    for rank in rank_count:
        if rank_count[rank] == 2:
            return "One Pair", rank
    return None

def high_card(cards):
    highest_card = max(cards, key=card_rank)  
    return "High Card", highest_card

def evaluate_hand(cards):
    rank_count = Counter(card[0] for card in cards)
    suit_count = Counter(card[1] for card in cards)

    result = straight_flush(cards, suit_count)
    if result:
        return result

    result = four_of_a_kind(rank_count)
    if result:
        return result

    result = full_house(rank_count)
    if result:
        return result

    result = flush(cards, suit_count)
    if result:
        return result

    result = is_straight(cards)
    if result:
        return result

    result = three_of_a_kind(rank_count)
    if result:
        return result

    result = two_pair(rank_count)
    if result:
        return result

    result = one_pair(rank_count)
    if result:
        return result

    return high_card(cards)
