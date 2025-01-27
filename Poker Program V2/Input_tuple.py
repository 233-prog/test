def get_user_cards(card_type, needed_cards):
    valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    valid_suits = ["S", "H", "D", "C"]

    while True:
        user_input = input(f"Enter the {card_type} cards : ").strip()
        cards_list = user_input.split()

        if len(cards_list) != needed_cards:
            print(f" You need to enter {needed_cards} cards. Try again!")
            continue
        
        is_valid = True
        cards = set()

        for card in cards_list:
            if len(card) != 2:
                is_valid = False
                break

            first_char = card[0]
            second_char = card[1]

            if first_char not in valid_ranks:
                is_valid = False
                break
            if second_char not in valid_suits:
                is_valid = False
                break

            if card in cards:
                print("Duplicate card found in user input. Please try again with different cards.")
                is_valid = False
                break

            cards.add(card)

        if is_valid:
            return [tuple(card) for card in cards_list]

        print("Make sure your cards are in the right format like XY XY.")

def get_community_cards():
    valid_numbers = [0, 3, 4, 5]
    community_cards = []

    while True:
        community_input = input("Enter the community cards: ").strip()

        if community_input:
            community_list = community_input.split()

            if len(community_list) in valid_numbers:
                community_card_tuples = []

                for card in community_list:
                    community_card_tuples.append(tuple(card))

                community_cards = community_card_tuples
                return community_cards
            else:
                print("The number of community cards must be 0, 3, 4, or 5. Please try again.")

        else:
            return community_cards

def validate_no_duplicates(user_cards, community_cards):
    all_cards = user_cards + community_cards
    seen_cards = set()

    for card in all_cards:
        if card in seen_cards:
            return False  
        seen_cards.add(card)
    
    return True

def main():
    user_cards = get_user_cards("user", 2)
    board_cards = get_community_cards()

    if not validate_no_duplicates(user_cards, board_cards):
        print("Duplicate cards detected. Please try again.")
        return

    print(f"Your cards are: {user_cards}")
    print(f"Community cards are: {board_cards}")

main()
