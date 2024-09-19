import math
import time

# Constants
PLAYER_X = "X"  # Human player
PLAYER_O = "O"  # AI player
EMPTY = " "  # Empty cell

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if the board is full
def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Function to check if there is a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

# Function to get available moves
def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_O:  # AI wins
        return 1
    elif winner == PLAYER_X:  # Human wins
        return -1
    elif is_full(board):  # Tie
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            r, c = move
            board[r][c] = PLAYER_O
            score = minimax(board, depth + 1, False)
            board[r][c] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            r, c = move
            board[r][c] = PLAYER_X
            score = minimax(board, depth + 1, True)
            board[r][c] = EMPTY
            best_score = min(best_score, score)
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    start_time = time.time()  # Start time for AI move calculation

    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        r, c = move
        board[r][c] = PLAYER_O
        score = minimax(board, 0, False)
        board[r][c] = EMPTY
        if score > best_score:
            best_score = score
            best_move = (r, c)

    end_time = time.time()  # End time for AI move calculation
    evaluation_time = round(end_time - start_time, 7)  # Calculate the time taken
    print(f"AI move evaluation time: {evaluation_time}s")  # Print the evaluation time

    return best_move, evaluation_time

# Main function to play the game
def play_game():
    board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
    current_player = PLAYER_O  # AI plays first

    total_ai_time = 0  # Total time for AI
    total_player_time = 0  # Total time for Player

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner or is_full(board):
            break

        if current_player == PLAYER_X:
            # Player's move
            print("Your turn!")
            start_time = time.time()  # Start time for player move
            move = input("Enter your move (row and column): ").split()
            move = (int(move[0]), int(move[1]))
            end_time = time.time()  # End time for player move
            player_time = round(end_time - start_time, 7)  # Calculate time for player's move
            print(f"Player move time: {player_time}s")
            total_player_time += player_time

        else:
            # AI's move
            print("AI's turn...")
            move, ai_time = find_best_move(board)
            total_ai_time += ai_time  # Add AI move time to total

        if board[move[0]][move[1]] == EMPTY:
            board[move[0]][move[1]] = current_player
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
        else:
            print("Invalid move! Try again.")

    print_board(board)
    if winner:
        print(f"Winner: {winner}")
    else:
        print("It's a tie!")

    # Print total time for AI and player separately
    print(f"Total AI time: {round(total_ai_time, 7)}s")
    print(f"Total Player time: {round(total_player_time, 7)}s")

if __name__ == "__main__":
    play_game()
