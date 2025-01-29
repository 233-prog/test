from collections import Counter

rank_value = {"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"J": 11,"Q": 12,"K": 13,"A": 14}

# This function checks if a list of ranks is in a row, like 5,6,7,8,9.
def sequence(ranks):
    rank_values_list = []
    for rank in ranks:
        rank_value = rank_value[rank]
        rank_values_list.append(rank_value)
    
    sorted_rank_values = sorted(rank_values_list)
    
    i = 0
    while i < len(sorted_rank_values) - 1:
        next_value = sorted_rank_values[i] + 1
        if next_value != sorted_rank_values[i + 1]:
            return False
        i = i + 1
    return True

# This function will figure out what poker hand you have from a list of 5 or more cards.
def rankings_hand(cards):
    # Let's pull out ranks and suits into their own lists.
    ranks_list = []
    suits_list = []
    for card in cards:
        # The rank is everything except the last character,
        # and the suit is the last character.
        rank_part = card[:-1]
        suit_part = card[-1]
        ranks_list.append(rank_part)
        suits_list.append(suit_part)
    
    rank_counts = Counter(ranks_list)
    suit_counts = Counter(suits_list)
    
    # 1) Check for a Straight Flush
    #    That means at least 5 cards of the same suit that are also in a row.
    for suit in suit_counts:
        if suit_counts[suit] >= 5:
            suited_cards = []
            for c in cards:
                if c[-1] == suit:
                    suited_cards.append(c)
            
            suited_ranks_list = []
            for c in suited_cards:
                rank_of_suited_card = c[:-1]
                suited_ranks_list.append(rank_of_suited_card)
            
            if sequence(suited_ranks_list):
                # We find the highest card among them
                # by looking at rank_to_value and picking the largest.
                i2 = 0
                highest_card = suited_ranks_list[i2]
                i2 = i2 + 1
                while i2 < len(suited_ranks_list):
                    if rank_value[suited_ranks_list[i2]] > rank_value[highest_card]:
                        highest_card = suited_ranks_list[i2]
                    i2 = i2 + 1
                return "Straight Flush"
    
    # 2) Check for Four of a Kind (4 cards of the same rank)
    for rank, count in rank_counts.items():
        if count == 4:
            return "Four of a Kind"
    
    # 3) Check for a Full House (3 of a kind + a pair)
    three_of_a_kind_rank = None
    pair_rank = None
    for rank, count in rank_counts.items():
        if count == 3:
            three_of_a_kind_rank = rank
        else:
            if count == 2:
                # We'll remember the pair
                pair_rank = rank
    
    if three_of_a_kind_rank is not None:
        if pair_rank is not None:
            return "Full House", three_of_a_kind_rank, pair_rank
    
    # 4) Check for a Flush (5 cards of the same suit)
    for suit_key, suit_count in suit_counts.items():
        if suit_count >= 5:
            # We only look at the cards that have this suit
            flush_cards = []
            for c in cards:
                if c[-1] == suit_key:
                    flush_cards.append(c)
            # We want to pick the top 5 in that suit by rank value
            sorted_flush_cards = sorted(flush_cards, key=lambda c: rank_value[c[:-1]], reverse=True)
            top_five = sorted_flush_cards[:5]
            return "Flush", top_five
    
    # 5) Check for a Straight (5 cards in a row, any suits)
    if sequence(ranks_list):
        # find highest card
        i3 = 0
        highest_straight_card = ranks_list[i3]
        i3 = i3 + 1
        while i3 < len(ranks_list):
            if rank_value[ranks_list[i3]] > rank_value[highest_straight_card]:
                highest_straight_card = ranks_list[i3]
            i3 = i3 + 1
        return "Straight"
    
    # 6) Check for Three of a Kind
    for rank, count in rank_counts.items():
        if count == 3:
            return "Three of a Kind", rank
    
    # 7) Check for Two Pair
    all_pairs = []
    for rank, count in rank_counts.items():
        if count == 2:
            all_pairs.append(rank)
    
    if len(all_pairs) >= 2:
        # We pick the top two pairs by rank value
        sorted_pairs = sorted(all_pairs, key=lambda r: rank_value[r], reverse=True)
        top_two = sorted_pairs[:2]
        return "Two Pair", top_two
    
    # 8) Check for One Pair
    for rank, count in rank_counts.items():
        if count == 2:
            return "One Pair", rank
    
    # 9) If none of those happen, we pick a High Card
    i4 = 0
    highest_card = ranks_list[i4]
    i4 = i4 + 1
    while i4 < len(ranks_list):
        if rank_value[ranks_list[i4]] > rank_value[highest_card]:
            highest_card = ranks_list[i4]
        i4 = i4 + 1
    return "High Card", highest_card

# Here's a test:
cards = ["10H", "JH", "JS", "JC", "AH"]
my_result = rankings_hand(cards)
print(my_result)
