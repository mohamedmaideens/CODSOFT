import math

# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to display the board
def display_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if a player has won
def check_winner(player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the board is full
def is_draw():
    return all(cell != " " for row in board for cell in row)

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):  # AI wins
        return 1
    if check_winner("X"):  # Human wins
        return -1
    if is_draw():  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        board[move[0]][move[1]] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    display_board()
    while True:
        # Human move
        try:
            x, y = map(int, input("Enter your move (row and column): ").split())
            if board[x][y] != " ":
                print("Cell already taken! Try again.")
                continue
            board[x][y] = "X"
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers (0, 1, or 2).")
            continue

        display_board()

        if check_winner("X"):
            print("Congratulations! You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        # AI move
        ai_move()
        print("AI's move:")
        display_board()

        if check_winner("O"):
            print("AI wins! Better luck next time.")
            break
        if is_draw():
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()