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

ranks_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def sort_cards(cards):
    n = len(cards)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            current_rank = ranks_order[cards[j][0]]
            next_rank = ranks_order[cards[j + 1][0]]
            if current_rank < next_rank:
                x = cards[j]              
                cards[j] = cards[j + 1]      
                cards[j + 1] = x       

def find_straight(cards, ranks_order):
    ranks = [] 
    
    for card in cards:
        rank = card[0]  
        if rank not in ranks:
            ranks.append(rank)

    rank_values = []  
    for rank in ranks:
        numeric_value = ranks_order[rank]  
        rank_values.append(numeric_value)

    n = len(rank_values)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if rank_values[j] < rank_values[j + 1]:
                temp = rank_values[j]
                rank_values[j] = rank_values[j + 1]
                rank_values[j + 1] = temp

    for i in range(len(rank_values) - 4):
        consecutive_count = 1
        for j in range(i, i + 4):
            if rank_values[j] - rank_values[j + 1] == 1:
                consecutive_count = consecutive_count + 1
            else:
                break  

        if consecutive_count == 5:
            return rank_values

def evaluate_hand(cards):
    rank_count = {}
    suit_count = {}

    for card in cards:
        rank, suit = card
        
        if rank not in rank_count:
            rank_count[rank] = 0
        rank_count[rank] = rank_count[rank] + 1
        
        if suit not in suit_count:
            suit_count[suit] = 0
        suit_count[suit] = suit_count[suit] + 1

    # STRAIGHT FLUSH
    for suit in suit_count:
        if suit_count[suit] >= 5:
            suited_cards = []
            for c in cards:
                if c[1] == suit:
                    suited_cards.append(c)
            sort_cards(suited_cards)

            straight_flush_result = find_straight(cards,ranks_order)
            if straight_flush_result is not None:
                return ("Straight Flush", straight_flush_result)

    # QUADS 
    for rank, count in rank_count.items():
        if count == 4:
            four_cards = []
            kickers = []
            
            for c in cards:
                if c[0] == rank and len(four_cards) < 4:
                    four_cards.append(c)
                else:
                    kickers.append(c)
    
            sort_cards(kickers)
            if len(kickers) > 0:
                best_kicker = kickers[0]
            else:
                best_kicker = None

            if best_kicker is not None:
                best_five = four_cards + [best_kicker]
            else:
                best_five = four_cards
            
            return ("Four of a Kind", best_five)

    # FULL HOUSE 
        three_list = []
    pair_list = []

    rank_index = 0
    rank_keys = []

    while rank_index < len(rank_count):
        rank_keys.append(list(rank_count)[rank_index])
        rank_index = rank_index + 1

    rank_index = 0

    while rank_index < len(rank_keys):
        rank = rank_keys[rank_index]
        count = rank_count[rank]
        
        if count == 3:
            three_list.append(rank)
        
        if count == 2:
            pair_list.append(rank)
        
        rank_index = rank_index + 1

    i = 0

    while i < len(three_list) - 1:
        j = 0
        
        while j < len(three_list) - 1 - i:
            rank1 = three_list[j]
            rank2 = three_list[j + 1]
            
            value1 = ranks_order[rank1]
            value2 = ranks_order[rank2]
            
            if value1 < value2:
                three_list[j] = rank2
                three_list[j + 1] = rank1
            
            j = j + 1
        
        i = i + 1

    i = 0

    while i < len(pair_list) - 1:
        j = 0
        
        while j < len(pair_list) - 1 - i:
            rank1 = pair_list[j]
            rank2 = pair_list[j + 1]
            
            value1 = ranks_order[rank1]
            value2 = ranks_order[rank2]
            
            if value1 < value2:
                pair_list[j] = rank2
                pair_list[j + 1] = rank1
            
            j = j + 1
        
        i = i + 1

    if len(three_list) >= 2:
        first_three = three_list[0]
        second_three = three_list[1]
        
        first_three_cards = []
        second_three_cards = []
        
        card_index = 0
        
        while card_index < len(cards):
            card = cards[card_index]
            card_rank = card[0]
            
            if card_rank == first_three and len(first_three_cards) < 3:
                first_three_cards.append(card)
            
            if card_rank == second_three and len(second_three_cards) < 3:
                second_three_cards.append(card)
            
            card_index = card_index + 1
        
        top_two = []
        top_index = 0
        
        while top_index < len(second_three_cards) and len(top_two) < 2:
            top_two.append(second_three_cards[top_index])
            top_index = top_index + 1
        
        return ("Full House", first_three_cards + top_two)

    if len(three_list) == 1 and len(pair_list) >= 1:
        first_three = three_list[0]
        first_pair = pair_list[0]
        
        best_three = []
        best_pair = []
        
        card_index = 0
        
        while card_index < len(cards):
            card = cards[card_index]
            card_rank = card[0]
            
            if card_rank == first_three and len(best_three) < 3:
                best_three.append(card)
            
            if card_rank == first_pair and len(best_pair) < 2:
                best_pair.append(card)
            
            card_index = card_index + 1
        
        return ("Full House", best_three + best_pair)

    # FLUSH
    for suit in suit_count:
        if suit_count[suit] >= 5:
            flush_cards = []
            
            for c in cards:
                if c[1] == suit:
                    flush_cards.append(c)
            sort_cards(flush_cards)
            
            top_five = []
            index = 0
            while index < 5 and index < len(flush_cards):
                top_five.append(flush_cards[index])
                index = index + 1
            
            return ("Flush", top_five)


    # STRAIGHT
        
    straight_result = find_straight(cards,ranks_order)
    if straight_result is not None:
        return ("Straight", straight_result)

    # TRIPS
    three_of_a_kind_found = False
    three_cards = []
    kickers = []

    for rank, count in rank_count.items():
        if count == 3:
            three_of_a_kind_found = True
            
            card_index = 0
            
            while card_index < len(cards):
                current_card = cards[card_index]
                
                if current_card[0] == rank:
                    if len(three_cards) < 3:
                        three_cards.append(current_card)
                    else:
                        kickers.append(current_card)
                else:
                    kickers.append(current_card)
                
                card_index = card_index + 1
            
            sort_cards(kickers)
            
            top_kickers = []
            kick_index = 0
            
            while kick_index < len(kickers) and len(top_kickers) < 2:
                top_kickers.append(kickers[kick_index])
                kick_index = kick_index + 1
            
            return ("Three of a Kind", three_cards + top_kickers)

    # TWO PAIR 
    pair_ranks = []
    for rank, count in rank_count.items():
        if count == 2:
            pair_ranks.append(rank)

        i = 0
    while i < len(pair_ranks) - 1:
        j = 0
        while j < len(pair_ranks) - 1 - i:
            current_rank = pair_ranks[j]
            next_rank = pair_ranks[j + 1]
            current_rank_value = ranks_order[current_rank]
            next_rank_value = ranks_order[next_rank]
            if current_rank_value < next_rank_value:
                pair_ranks[j] = next_rank
                pair_ranks[j + 1] = current_rank 
            j = j + 1
        i = i + 1

    pair_count = len(pair_ranks)
    if pair_count >= 2:
        pair1 = pair_ranks[0]
        pair2 = pair_ranks[1]
        
        pair1_cards = []
        pair2_cards = []
        kickers = []
        
        card_index = 0
        
        while card_index < len(cards):
            current_card = cards[card_index]
            current_card_rank = current_card[0]
            
            if current_card_rank == pair1 and len(pair1_cards) < 2:
                pair1_cards.append(current_card)
            elif current_card_rank == pair2 and len(pair2_cards) < 2:
                pair2_cards.append(current_card)
            else:
                kickers.append(current_card)
            
            card_index = card_index + 1
        
        sort_cards(kickers)
        
        top_kicker = []
        kicker_index = 0
        
        while kicker_index < len(kickers) and len(top_kicker) < 1:
            top_kicker.append(kickers[kicker_index])
            kicker_index = kicker_index + 1
        
        best_five_cards = pair1_cards + pair2_cards + top_kicker
        
        return ("Two Pair", best_five_cards)

    # ONE PAIR 
    pair_found = False
    pair_cards = []
    kickers = []

    rank_items = []
    rank_index = 0

    while rank_index < len(rank_count):
        rank_key = list(rank_count)[rank_index]  
        rank_value = rank_count[rank_key]        
        rank_items.append((rank_key, rank_value))  
        rank_index = rank_index + 1

    rank_index = 0

    while rank_index < len(rank_items):
        rank = rank_items[rank_index][0]
        count = rank_items[rank_index][1]
        
        if count == 2 and not pair_found:
            pair_found = True
            
            card_index = 0
            
            while card_index < len(cards):
                current_card = cards[card_index]
                current_rank = current_card[0]
                
                if current_rank == rank and len(pair_cards) < 2:
                    pair_cards.append(current_card)
                else:
                    kickers.append(current_card)
                
                card_index = card_index + 1
            
            sort_cards(kickers)
            
            top_kickers = []
            kicker_index = 0
            
            while kicker_index < len(kickers) and len(top_kickers) < 3:
                top_kickers.append(kickers[kicker_index])
                kicker_index = kicker_index + 1
            
            best_five_cards = pair_cards + top_kickers
            
            return ("One Pair", best_five_cards)
        
        rank_index = rank_index + 1


    # HIGH CARD
    sort_cards(cards)
    high_card_hand = []
    index = 0
    while index < 5 and index < len(cards):
        high_card_hand.append(cards[index])
        index = index + 1

    return ("High Card", high_card_hand)

def process_input():
    full_hand = []
    index = 0

    while index < len(user_cards_tuples):
        full_hand.append(user_cards_tuples[index])
        index = index + 1

    index = 0

    while index < len(board_cards_tuples):
        full_hand.append(board_cards_tuples[index])
        index = index + 1

    hand_ranking = evaluate_hand(full_hand)

    hand_type = hand_ranking[0]

    hand_ranking_map = {"Straight Flush": 1,"Four of a Kind": 2,"Full House": 3,"Flush": 4,"Straight": 5,"Three of a Kind": 6,"Two Pair": 7,"One Pair": 8, "High Card": 9}

    print((hand_type, hand_ranking_map[hand_type]))

    if len(hand_ranking) > 1:
        best_cards = hand_ranking[1]

        if isinstance(best_cards, list):
            print(tuple(best_cards))  

process_input()
