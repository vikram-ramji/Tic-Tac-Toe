class Board:
    BOARD_SIZE = 3

    def __init__(self):
        self.board = [[" " for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]

    def __getitem__(self, index):
        return self.board[index]

    def __setitem__(self, index, value):
        self.board[index] = value

    def display_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * (self.BOARD_SIZE * 2 - 1))

class Engine:
    def __init__(self):
        self.players = ["X","O"]
        self.current_player = 0
    
    def get_player(self):
        return self.players[self.current_player]

    def take_user_input(self):
        row = int(input("Enter row (0, 1, or 2): "))
        column = int(input("Enter column (0, 1, or 2): "))
        return row, column
    
    def check_win(self, board, player):
        for i in range(3):
            if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
            return True
        return False
    
    def check_draw(self, board):
        empty_cells = {(i, j) for i in range(3) for j in range(3) if not board[i][j]}
        return not empty_cells

def main():
    board = Board()
    engine = Engine()

    while True:
        board.display_board()
        player = engine.get_player()
        print(f"Current player -> {player}")

        try:
            row, column = engine.take_user_input()   
            if not board[row][column]:
                board[row][column] = player
                if engine.check_win(board, player):
                    board.display_board()
                    print(f"Player {player} won!")
                    break
                elif engine.check_draw(board):
                    board.display_board()
                    print("It's a draw.")
                    break
                engine.current_player = (engine.current_player + 1) % 2
            else:
                print("Cell's already occupied. Please try again!!")
        except ValueError:
            print("Invalid Input. Try again!!")
        except IndexError:
            print(f"Entered row or column number out of range. Please enter a number between 0 and {Board.BOARD_SIZE-1}")
        except KeyboardInterrupt:
            print("Game interrupted by user.")
            break
        except EOFError:
            print("End of input reached. Exiting game.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    play_again = input("Do you want to play again? If yes, enter 'yes' : ")
    if play_again.lower() == 'yes':
        main()