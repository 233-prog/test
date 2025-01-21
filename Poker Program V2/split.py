user_cards_input = input("Enter your two cards: ")

board_cards_input = input("Enter the board cards: ")

user_cards_list = user_cards_input.split()
board_cards_list = board_cards_input.split()

user_card_tuples = []
for card in user_cards_list:
    value = card[:-1] 
    suit = card[-1]    
    user_card_tuples.append((value, suit))  


board_card_tuples = []
for card in board_cards_list:
    value = card[:-1]  
    suit = card[-1]  
    board_card_tuples.append((value, suit))  

print("User Cards:")
print(user_card_tuples)

print("Board Cards:")
print(board_card_tuples)
