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

ranks_order = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def card_rank(card):
    return ranks_order[card[0]]

def card_rank_descending(card):
    return -ranks_order[card[0]]

def get_highest_five(cards):
    return sorted(cards, key=card_rank_descending)[:5]

def is_straight(cards):
    cards.sort(key=card_rank_descending)
    for i in range(len(cards) - 4):
        if ranks_order[cards[i][0]] - ranks_order[cards[i + 4][0]] == 4:
            return True
    return False

def evaluate_hand(cards):
    rank_count = {}
    suit_count = {}

    for card in cards:
        rank, suit = card
        if rank in rank_count:
            rank_count[rank] += 1
        else:
            rank_count[rank] = 1
        
        if suit in suit_count:
            suit_count[suit] += 1
        else:
            suit_count[suit] = 1
#STRAIGHT FLUSH
    for suit in suit_count:
        if suit_count[suit] >= 5:
            suited_cards = [card for card in cards if card[1] == suit]
            if is_straight(suited_cards):
                sequence = get_highest_five(suited_cards)
                return "Straight Flush", sequence
#QUADS
    for rank, count in rank_count.items():
        if count == 4:
            return "Four of a Kind", rank
#FH
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
        pair = pair_list[0] if len(pair_list) > 0 else None
        return "Full House", trips, pair
#FLUSH
    for suit in suit_count:
        if suit_count[suit] >= 5:
            flush_cards = [card for card in cards if card[1] == suit]
            flush_cards = get_highest_five(flush_cards)
            return "Flush", flush_cards
#STRAIGHT
    if is_straight(cards):
        sequence = get_highest_five(cards)
        return "Straight", sequence
#TRIPS
    for rank, count in rank_count.items():
        if count == 3:
            return "Three of a Kind", rank
#DOUBLE PAIR
    pair_ranks = [rank for rank, count in rank_count.items() if count == 2]
    if len(pair_ranks) >= 2:
        pair_ranks.sort(reverse=True)
        return "Two Pair", pair_ranks[0], pair_ranks[1]
#ONE PAIR
    for rank, count in rank_count.items():
        if count == 2:
            return "One Pair", rank
#HIGH CARD
    highest_card = max(cards, key=card_rank)
    return "High Card", highest_card

def process_input():
    full_hand = board_cards_tuples + user_cards_tuples
    hand_ranking = evaluate_hand(full_hand)
    print(f"Hand ranking: {hand_ranking[0]}")
    
    if len(hand_ranking) > 2:
        print("Cards in the hand:", hand_ranking[2])


process_input()
