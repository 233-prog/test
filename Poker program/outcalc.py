from itertools import product

# Function to generate the full deck
def generate_full_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["S", "H", "D", "C"]
    return [rank + suit for rank, suit in product(ranks, suits)]

# Function to evaluate hand strength (placeholder)
def evaluate_hand(hand):
    # Replace this function with proper hand evaluation logic
    # Return a numeric score representing the strength of the hand
    return len(hand)  # Simplified example

# Function to calculate outs
def calculate_outs(player_hand, board_cards):
    # Generate the full deck and calculate the remaining deck
    full_deck = generate_full_deck()
    remaining_deck = [card for card in full_deck if card not in player_hand + board_cards]

    # Evaluate the current best hand
    current_best_hand = evaluate_hand(player_hand + board_cards)

    # Initialize outs list
    outs = []

    # Loop through remaining cards and evaluate new hands
    for card in remaining_deck:
        temp_board = board_cards + [card]
        new_hand = evaluate_hand(player_hand + temp_board)

        # Check if the new hand is better than the current best hand
        if new_hand > current_best_hand:
            outs.append(card)

    return outs

# Function to calculate probabilities for outs
def calculate_out_probabilities(outs, unseen_cards):
    # Total number of unseen cards
    total_unseen = len(unseen_cards)

    # Calculate probabilities for each out
    probabilities = {out: 1 / total_unseen for out in outs}

    return probabilities

# Example Usage
player_hand = ["10H", "JD"]
board_cards = ["JS", "JD", "10C"]

# Calculate outs
outs = calculate_outs(player_hand, board_cards)

# Calculate probabilities
full_deck = generate_full_deck()
unseen_cards = [card for card in full_deck if card not in player_hand + board_cards]
probabilities = calculate_out_probabilities(outs, unseen_cards)

# Print results
print("Outs:", outs)
print("Probabilities:", probabilities)
