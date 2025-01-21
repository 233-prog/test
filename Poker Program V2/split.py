user_cards_input = input("Enter your two cards: ")

board_cards_input = input("Enter the board cards: ")

user_cards_list = user_cards_input.split()
board_cards_list = board_cards_input.split()

user_card_tuples = [(card[:-1], card[-1]) for card in user_cards_list]
board_card_tuples = [(card[:-1], card[-1]) for card in board_cards_list]

print("User Cards:")
print(user_card_tuples)

print("Board Cards:")
print(board_card_tuples)
