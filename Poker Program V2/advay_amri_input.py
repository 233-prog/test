def validate_card(card):
    valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    valid_suits = ["S", "H", "D", "C"]
    
    if len(card) != 2:
        return False
    if card[0] not in valid_ranks:
        return False
    if card[1] not in valid_suits:
        return False
    return True

def validate_input(users_cards_input, community_cards_input):

    users_cards = []
    community_cards = []

    user_cards_list = users_cards_input.split()

    if len(user_cards_list) != 2:
        print("Invalid number of cards in user's hand. Please enter two cards.")        
        return False, [], []
    else:

        card = user_cards_list[0]
        rank = card[:-1]
        suit = card[-1]
        first_card = (rank, suit)

        card = user_cards_list[1]
        rank = card[:-1]
        suit = card[-1]
        second_card = (rank, suit)

        if validate_card(first_card) and validate_card(second_card):
            users_cards.append(first_card)
            users_cards.append(second_card)
        else:
            print("Invalid card in user's hand. Please enter a valid card.")
            return False, [], []

    community_cards_list = community_cards_input.split()
    
    if len(community_cards_list) not in [0, 3, 4, 5]:
        print("Invalid number of community cards. Please enter 0, 3, 4, or 5 cards.")
        return False, [], []
    
    for card in community_cards_list:
        rank = card[:-1]
        suit = card[-1]

        if validate_card((rank, suit)):
            community_cards.append((rank, suit))
        else:
            print("Invalid card in community cards. Please enter a valid card.")
            return False, [], []
        
    if len(users_cards + community_cards) != len(set(users_cards + community_cards)):
        print("Invalid cards. Please enter unique cards.")
        return False, [], []

    return True, users_cards, community_cards

def get_user_input():
    users_cards = []
    community_cards = []

    while True:
        users_cards_input = input("Enter your two cards:")
        community_cards_input = input("Enter the community cards:")
        valid, users_cards, community_cards = validate_input(users_cards_input, community_cards_input)

        if valid == True:
            break

    return users_cards, community_cards

if __name__ == "__main__":
    users_cards, community_cards = get_user_input()
    print(f"Users cards: {users_cards}")
    print(f"Community cards: {community_cards}")