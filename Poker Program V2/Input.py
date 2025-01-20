print("Enter the rank of the first card")
first_card_rank = input("Type the rank: ")
first_card_rank = first_card_rank.strip()

print("Enter the suit of the first card")
first_card_suit = input("Type the suit (S, H, D, C): ")
first_card_suit = first_card_suit.strip()

valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
valid_suits = ["S", "H", "D", "C"]
valid_board = [0, 3, 4, 5]

while first_card_rank not in valid_ranks:
    print("That rank is wrong. Please try again.")
    first_card_rank = input("Type the rank (2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A): ")
    first_card_rank = first_card_rank.strip()

while first_card_suit not in valid_suits:
    print("That suit is not correct. Please try again.")
    first_card_suit = input("Type the suit (S, H, D, C): ")
    first_card_suit = first_card_suit.strip()

print("Enter the rank of the second card")
second_card_rank = input("Type the rank: ") 
second_card_rank = second_card_rank.strip()

print("Enter the suit of the second card")
second_card_suit = input("Type the suit (S, H, D, C): ")
second_card_suit = second_card_suit.strip()

while second_card_rank not in valid_ranks:
    print("That rank is wrong. Please try again.")
    second_card_rank = input("Type the rank (2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A): ")
    second_card_rank = second_card_rank.strip()

while second_card_suit not in valid_suits:
    print("That suit is not correct. Please try again.")
    second_card_suit = input("Type the suit (S, H, D, C): ")
    second_card_suit = second_card_suit.strip()

board_count_input = input("How many community cards do you want to enter (0, 3, 4, 5)? ").strip()
board_count = int(board_count_input)

while board_count not in valid_board:
    print("Invalid number of community cards. Valid options are: 0, 3, 4, 5.")
    board_count_input = input("How many community cards do you want to enter (0, 3, 4, 5)? ").strip()
    board_count = int(board_count_input)

board_cards = []

if board_count > 0:
    print(f"\nEnter the {board_count} community card(s).")
    for i in range(board_count):
        print(f" Community card {i+1}")
        
        rank = input("Enter the rank: ").strip()
        while rank not in valid_ranks:
            print("Invalid rank. Please try again.")
            rank = input("Enter the rank (2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A): ").strip()

        suit = input("Enter the suit (S, H, D, C): ").strip()
        while suit not in valid_suits:
            print("Invalid suit. Please try again.")
            suit = input("Enter the suit (S, H, D, C): ").strip()
        
        board_cards.append((rank, suit))

print(f"The first card is: {first_card_rank}{first_card_suit}, "
      f"The second card is: {second_card_rank}{second_card_suit}")
print(f"Number of community cards: {board_count}")
print(f"Community Cards: {board_cards}")