from random import shuffle, sample
from collections import Counter
from os import system
from  termcolor import colored

class Board():
    '''This class illustrates sudoku game'''
    def __init__(self):
        '''self.board_chart is attribute that their values were made by creat board() method 
        and gives us initial values so that player can start game'''
        self.board_chart = self.create_board()

    def create_board(self):
        '''the stracture of this method includes 9 squares. At first one list was considered that is
        consisted 9 list that have values in range(1-9). after that these values of each squares were 
        designed as no same vlues must be located in same-row and and same column and square and 5 numbers of 
        each suare whoes vlues turn into empty randomly till player can gusse in game'''
        sq = [""]*9
        while True:
            for i in range(9):
                sq[i]=list(range(1,10))
                shuffle(sq[i])
                rand_index = sample(range(9), 5)
                for index in rand_index:
                    sq[i][index] = " "
            self.test = sq
            if self.board_checker(sq):
                return sq
        
    
    def board_checker(self, sq):
        '''duty of board_checker() is whenever player enter number or at the begining of game
        keep checking there is no equal value in same row and column'''
        comp = list(range(1,10))
        # column
        for x in range(3):
            for j in range(3):
                s = []
                for i in range(0,9,3):
                        s.append(sq[i+x][0+j])
                        s.append(sq[i+x][3+j])
                        s.append(sq[i+x][6+j])
                else:
                    for c in comp:
                        if s.count(c) > 1:
                            return False

        else:
            # row
            for x in range(0,9,3):

                for j in range(0,9,3):
                    s = []
                    for i in range(3):
                            s.append(sq[x+i][0+j])
                            s.append(sq[x+i][1+j])
                            s.append(sq[x+i][2+j])

                    else:
                        for c in comp:
                            if s.count(c) > 1:
                                return False

            else: 
                return True

    
    def __str__(self):
        '''print board of sudoku game'''
        s_dash = colored("-"*55+"\n", 'red')
        s_star = colored("*"*55+"\n", 'green')
        s_total = "\n\n"+s_star
        s_col = [i for i in range(9)]
        s_col1 = colored(f"column=> {s_col[0]}   {s_col[1]}   {s_col[2]}         {s_col[0]}   {s_col[1]}   {s_col[2]}         {s_col[0]}   {s_col[1]}   {s_col[2]}\n", 'yellow')
        s_col2 = colored(f"column=> {s_col[3]}   {s_col[4]}   {s_col[5]}         {s_col[3]}   {s_col[4]}   {s_col[5]}         {s_col[3]}   {s_col[4]}   {s_col[5]}\n", 'yellow')
        s_col3 = colored(f"column=> {s_col[6]}   {s_col[7]}   {s_col[8]}         {s_col[6]}   {s_col[7]}   {s_col[8]}         {s_col[6]}   {s_col[7]}   {s_col[8]}\n", 'yellow')
        for i in range(0,9,3):
            s1 = f"      || {self.test[i][0]} | {self.test[i][1]} | {self.test[i][2]} ||   || {self.test[i+1][0]} | {self.test[i+1][1]} | {self.test[i+1][2]} ||   || {self.test[i+2][0]} | {self.test[i+2][1]} | {self.test[i+2][2]}\n"
            s2 = colored(f"row=>{i}|",'magenta') + f"| {self.test[i][3]} | {self.test[i][4]} | {self.test[i][5]} |" + colored(f"|*{i+1}*|",'magenta') + f"| {self.test[i+1][3]} | {self.test[i+1][4]} | {self.test[i+1][5]} |" + colored(f"|*{i+2}*|",'magenta') + f"| {self.test[i+2][3]} | {self.test[i+2][4]} | {self.test[i+2][5]}\n"
            s3 = f"      || {self.test[i][6]} | {self.test[i][7]} | {self.test[i][8]} ||   || {self.test[i+1][6]} | {self.test[i+1][7]} | {self.test[i+1][8]} ||   || {self.test[i+2][6]} | {self.test[i+2][7]} | {self.test[i+2][8]}\n"
            s_total += s_col1+s_dash+s1+s_dash+s_col2+s_dash+s2+s_dash+s_col3+s_dash+s3+s_star
        system("cls")
        return s_total
    
    def full_place(self):
        '''full_place() cheks empety place in game'''
        for i in range(9):
            for j in range(9):
                if self.board_chart[i][j] == ' ':
                    return False
        else: return True


