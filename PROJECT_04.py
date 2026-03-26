# Tic Tac Toe game in Python

# Function to print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full
def board_full(board):
    return " " not in board

# Main game function
def tic_tac_toe():
    board = [" "] * 9  # The board is a list with 9 empty spaces
    current_player = "X"  # Player X starts
    while True:
        print_board(board)
        
        # Ask for the player's move
        move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
        
        # Validate the move
        if board[move] != " ":
            print("This position is already taken! Try again.")
            continue
        
        # Make the move
        board[move] = current_player
        
        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie (board is full)
        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
