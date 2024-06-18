
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, mark):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [mark, mark, mark] in win_conditions

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["Upin", "Ipin"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        try:
            row = int(input(f"{player}'s turn. Enter row (0, 1, 2): "))
            col = int(input(f"{player}'s turn. Enter column (0, 1, 2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board, player):
                    print_board(board)
                    print(f"{player} wins!")
                    break
                elif all(cell != " " for row in board for cell in row):
                    print_board(board)
                    print("It's a tie!")
                    break
                turn += 1
            else:
                print("Cell already taken. Try again.")
        else:
            print("Invalid row or column. Try again.")

tic_tac_toe()
