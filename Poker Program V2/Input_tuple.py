def get_user_cards(card_type, needed_cards):
    valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    valid_suits = ["S", "H", "D", "C"]

    while True:
        user_input = input(f"Enter the {card_type} cards : ").strip()
        cards_list = user_input.split()

        if len(cards_list) != needed_cards:
            print(f" You need to enter exactly {needed_cards} cards. Try again!")
            continue
        
        is_valid = True
        cards = set()
        
        for card in cards:
            if len(card) != 2:
                is_valid = False
                break

            first_char, second_char = card[0], card[1]

            if first_char not in valid_ranks or second_char not in valid_suits:
                is_valid = False
                break

            if card in cards:
                print("Please try again with different cards.")
                is_valid = False
                break
            
            cards.add(card)

        if is_valid:
            return [tuple(card) for card in cards_list]

        print("Something went wrong. Make sure your cards are in the right format like XY XY.")

def get_community_cards():
    valid_numbers = [0, 3, 4, 5]
    community_cards = []

    community_input = input("Enter the community cards: ").strip()

    if community_input:
        community_list = community_input.split()

        if len(community_list) in valid_numbers:
            community_cards = [tuple(card) for card in community_list]
        else:
            print("The number of community cards must be 0, 3, 4, or 5. Try again.")
            return get_community_cards()

    return community_cards

def main():
    user_cards = get_user_cards("user", 2)
    board_cards = get_community_cards()
    
    print(f"Your cards are: {user_cards}")
    print(f"Community cards are: {board_cards}")

main()
