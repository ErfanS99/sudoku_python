from game_package.main_Board import Board

class Player():
    '''this object due to give number from player and put there created'''
    def __init__(self, board: Board):
        '''self.boadr is attribute from class Board()
        self score is attribute as errore rate that player can be committed
        self.ans is attribute to evaluate player whose desiring to play again'''
        self.board = board
        self.score = 0
        self.ans = None

    def check(self):
        '''check() analyse that does not exist any equal value in each squares when player enter 
        number '''
        comp = list(range(1,10))
        for i in range(9):
            for c in comp:
                if self.board.board_chart[i].count(c) > 1:
                    return False

            else: return True

    def input_player(self):
        '''input_player() gives position and number from player and count number of player 
        when enter wrong wrong value'''
        try:
            pos_r,pos_c = map(int,input("enter row and column position: "))
            num = int(input("enter a number in range(1-9): "))
            if pos_r in range(9) and pos_c in range(9) and num in range(1,10):
                if self.board.board_chart[pos_r][pos_c] == ' ':
                    self.board.board_chart[pos_r][pos_c] = num
                    if self.check() and self.board.board_checker(self.board.board_chart):
                        print(self.board)
                        return True
                    else: 
                        self.score += 1
                        if self.score == 5:
                            print("game over!")
                            self.replay()
                        elif self.score < 5:
                            print(f"you lost: {self.score} out of 5")
                            self.board.board_chart[pos_r][pos_c] = ' '
                            self.input_player()
                else:
                    print("you can not enter here, enter again!")
                    self.input_player()
            else:
                print("you entered wrong, enter again!")
                self.input_player()
        except ValueError:
            print("you entered wrong, enter again!")
            self.input_player()

    def replay(self):
        '''replay() ask from player to play again'''
        self.ans = input('would you like to play again?(y/n): ').lower()
        if self.ans == 'n':
            return False
        elif self.ans != 'y':
            print("you entered wrong, please enter again!")
            self.replay()
        elif self.ans == 'y':
            return True