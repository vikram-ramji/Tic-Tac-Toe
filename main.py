def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def take_user_input():
    row = int(input("Enter row (0, 1, or 2): "))
    column = int(input("Enter column (0, 1, or 2): "))
    return row, column


def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def check_draw(board):
    return all(cell != " " for row in board for cell in row)


def reset_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def main():
    board = reset_board()
    players = ["X","O"]
    current_player = 0

    game_is_on = True
    while game_is_on:
        display_board(board)
        player = players[current_player]
        print(f"Current player -> {player}")

        try:
            row, column = take_user_input()
        except ValueError:
            print("Invalid Input. Try again!!")
            continue

        try:    
            if board[row][column] == " ":
                board[row][column] = player
                if check_win(board, player):
                    display_board(board)
                    print(f"Player {player} won!")
                    game_is_on = False
                elif check_draw(board):
                    display_board(board)
                    print("It's a draw.")
                    game_is_on = False
                current_player = (current_player + 1) % 2
            else:
                print("Cell's already occupied. Please try again!!")
        except IndexError:
                print("Entered row or column number out of range. Please try again")
                continue
        finally:
            if game_is_on == False:
                user_choice = int(input("Do you want to play again? If yes, enter 1 : "))
                if user_choice == 1:
                    game_is_on = True
                    board = reset_board()


if __name__ == "__main__":
    main()
