import random

# Initialize the game board
board = [' ' for _ in range(9)]  # A list to represent a 3x3 board

# Define possible winning combinations
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)  # Diagonals
]

# Function to print the current board
def print_board():
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

# Check if a player has won
def check_win(player):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Check if the board is full
def is_board_full():
    return ' ' not in board

# Minimax Algorithm to find the best move for the computer
def minimax(board, depth, is_maximizing):
    # Check if game is over
    if check_win('O'):
        return 1  # Computer wins
    if check_win('X'):
        return -1  # Player wins
    if is_board_full():
        return 0  # Tie

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # Computer move
                eval = minimax(board, depth + 1, False)
                board[i] = ' '  # Undo move
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # Player move
                eval = minimax(board, depth + 1, True)
                board[i] = ' '  # Undo move
                min_eval = min(min_eval, eval)
        return min_eval

# Find the best move for the computer
def computer_move():
    best_move = -1
    best_value = float('-inf')

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'  # Simulate computer move
            move_value = minimax(board, 0, False)
            board[i] = ' '  # Undo move

            if move_value > best_value:
                best_value = move_value
                best_move = i

    return best_move

# Player's move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                return move
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    current_player = 'X'  # Player is 'X', Computer is 'O'
    print_board()

    while True:
        if current_player == 'X':  # Player's turn
            move = player_move()
            board[move] = 'X'
        else:  # Computer's turn
            move = computer_move()
            board[move] = 'O'
            print(f"Computer's move: {move + 1}")
        
        print_board()

        # Check if someone has won
        if check_win('X'):
            print("You win!")
            break
        elif check_win('O'):
            print("Computer wins!")
            break
        elif is_board_full():
            print("It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()
