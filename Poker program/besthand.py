def calculate_hit_probability(player_hand, board_cards, target_hand, remaining_deck):
    
    # Determine the best possible hand the player can achieve and the cards required to form it.
    best_possible_hand, required_cards = rankings_hand(player_hand, board_cards, remaining_deck)

    # Check if the best possible hand matches the target hand
    if best_possible_hand == target_hand:
        # Calculate the probability based on the required cards
        number_of_outs = len(required_cards)
        total_unseen_cards = len(remaining_deck)

        # Probability = (Number of Outs) / (Total Unseen Cards) * 100
        probability = (number_of_outs / total_unseen_cards) * 100 if total_unseen_cards > 0 else 0
    else:
        probability = 0

    return probability, best_possible_hand, required_cards
