from collections import Counter

# Helper function to check for sequential cards
def is_sequential(ranks):
    """Check if a list of ranks forms a sequence."""
    rank_values = sorted([rank_to_value[rank] for rank in ranks])
    for i in range(len(rank_values) - 1):
        if rank_values[i] + 1 != rank_values[i + 1]:
            return False
    return True

# Helper function to convert ranks to values
rank_to_value = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
}

# Main function to rank the hand
def rankings_hand(cards):
    # Split cards into ranks and suits
    ranks = [card[:-1] for card in cards]
    suits = [card[-1] for card in cards]

    # Count occurrences of each rank and suit
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)

    # Check for a straight flush
    for suit in suit_counts:
        if suit_counts[suit] >= 5:
            suited_cards = [card for card in cards if card[-1] == suit]
            suited_ranks = [card[:-1] for card in suited_cards]
            if is_sequential(suited_ranks):
                highest_card = max(suited_ranks, key=lambda r: rank_to_value[r])
                return "Straight Flush", highest_card

    # Check for four of a kind
    for rank, count in rank_counts.items():
        if count == 4:
            return "Four of a Kind", rank

    # Check for full house
    three_of_a_kind = None
    pair = None
    for rank, count in rank_counts.items():
        if count == 3:
            three_of_a_kind = rank
        elif count == 2:
            pair = rank
    if three_of_a_kind and pair:
        return "Full House", three_of_a_kind, pair

    # Check for flush
    for suit, count in suit_counts.items():
        if count >= 5:
            suited_cards = [card for card in cards if card[-1] == suit]
            top_5_cards = sorted(suited_cards, key=lambda c: rank_to_value[c[:-1]], reverse=True)[:5]
            return "Flush", top_5_cards

    # Check for straight
    if is_sequential(ranks):
        highest_card = max(ranks, key=lambda r: rank_to_value[r])
        return "Straight", highest_card

    # Check for three of a kind
    for rank, count in rank_counts.items():
        if count == 3:
            return "Three of a Kind", rank

    # Check for two pair
    pairs = [rank for rank, count in rank_counts.items() if count == 2]
    if len(pairs) >= 2:
        top_two_pairs = sorted(pairs, key=lambda r: rank_to_value[r], reverse=True)[:2]
        return "Two Pair", top_two_pairs

    # Check for one pair
    for rank, count in rank_counts.items():
        if count == 2:
            return "One Pair", rank

    # High card
    highest_card = max(ranks, key=lambda r: rank_to_value[r])
    return "High Card", highest_card

# Example Usage
cards = ["10H", "JH", "JS", "JC", "10C"]  
result = rankings_hand(cards)
print(result)
