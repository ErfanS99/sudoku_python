from game_package.main_Board import Board
from game_package.main_Player import Player

def main():
    '''main() is major function to run the game'''
    print('welcome to Sudoku')
    board = Board()
    player = Player(board)
    print(board)

    while True:
        # bottom condition check existing empty place if not there is no place print you won'''
        if board.full_place():
            print("you won!")
            # if player won mottom method evoke from Player()
            if not player.replay():
                break
        if not player.input_player():
            break