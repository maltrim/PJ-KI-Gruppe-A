import random
from main import generate_gameboard2, get_move_list, switch_char2

class AI:
    def __init__(self, name):
        self.name = name # Farbe
        
    def determine_next_move(self):
        move_list = get_move_list(game.board, self.name)
        move_list.pop(0) # Count entfernen
        if move_list:
            return random.choice(move_list)
        else:
            return None # keine gültigen Züge
    
class Game:
    def __init__(self, p1, p2):
        self.board = generate_gameboard2()
        self.players = [p1, p2]
        self.current_player_index = 0
        
    def make_move(self, move):
        # Zerlege den Zug in seine Bestandteile
        start_pos, end_pos = move.split('-')
        start_x = switch_char2(start_pos[0])
        start_y = int(start_pos[1]) - 1
        end_x = switch_char2(end_pos[0])
        end_y = int(end_pos[1]) - 1
        
        # Zielfeld ist frei:
        if (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'b'):
            self.board[end_y][end_x] ='b'
            self.board[start_y][start_x] = ''
        elif (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'r'):
            self.board[end_y][end_x] ='r'
            self.board[start_y][start_x] = ''
        elif (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'rr'):
            self.board[end_y][end_x] ='r'
            self.board[start_y][start_x] = 'r'
        elif (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'bb'):
            self.board[end_y][end_x] ='b'
            self.board[start_y][start_x] = 'b'
        elif (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'rb'):
            self.board[end_y][end_x] ='b'
            self.board[start_y][start_x] = 'r'
        elif (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'br'):
            self.board[end_y][end_x] ='r'
            self.board[start_y][start_x] = 'b'
            
        # Zielfeld hat ein Stein:
        if (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'r'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = ''
        elif (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'b'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = ''
        elif (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'br'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = 'b'
        elif (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'rb'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = 'r'
        elif (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'bb'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = 'b'
        elif (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'rr'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = 'r'
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'r'): # ab hier mit blau als ziel
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = ''
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'b'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = ''
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'rb'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = 'r'
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'br'):
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = 'b'
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'bb'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = 'b'
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'rr'):
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = 'r'
            
        # Zielfeld hat zwei Steine:
        if (self.board[end_y][end_x] == 'rr' and self.board[start_y][start_x] == 'b'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = ''
        elif (self.board[end_y][end_x] == 'rr' and self.board[start_y][start_x] == 'bb'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = 'b'
        elif (self.board[end_y][end_x] == 'rr' and self.board[start_y][start_x] == 'rb'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = 'r'
        elif (self.board[end_y][end_x] == 'rb' and self.board[start_y][start_x] == 'r'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = ''
        elif (self.board[end_y][end_x] == 'rb' and self.board[start_y][start_x] == 'rr'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = 'r'
        elif (self.board[end_y][end_x] == 'rb' and self.board[start_y][start_x] == 'br'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = 'b'
        elif (self.board[end_y][end_x] == 'br' and self.board[start_y][start_x] == 'b'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = ''
        elif (self.board[end_y][end_x] == 'br' and self.board[start_y][start_x] == 'bb'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = 'b'
        elif (self.board[end_y][end_x] == 'br' and self.board[start_y][start_x] == 'rb'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = 'r'
        elif (self.board[end_y][end_x] == 'bb' and self.board[start_y][start_x] == 'r'):
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = ''
        elif (self.board[end_y][end_x] == 'bb' and self.board[start_y][start_x] == 'rr'):
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = 'r'
        elif (self.board[end_y][end_x] == 'bb' and self.board[start_y][start_x] == 'br'):
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = 'b'
        
    def is_game_over(self):
        gameboard = self.board
        turn = self.players[self.current_player_index].name
        
        if turn == 'r':
            opponent = ['b','rb','bb']
            opponent_row = 0
        elif turn == 'b':
            opponent = ['r','br','rr']
            opponent_row = 7

        # no figures left
        for opp in opponent:
            opponent_figures_remaining = any(opp in row for row in gameboard)
            if not opponent_figures_remaining:
                return True
        
        #no opponents moves left
        for opp in opponent:
            opponent_moves_available = any(get_move_list(gameboard, opp))
            if not opponent_moves_available:
                return True
        
        #reach opponent last row
        for row in gameboard:
            for opp in opponent:
                if opp in row:
                    if opponent_row == row:
                        return True
                
        return False
            
    def play(self):
        while not self.is_game_over():
            print(self.board)
            current_player = self.players[self.current_player_index]
            next_move = current_player.determine_next_move()
            self.make_move(next_move)
            self.current_player_index = (self.current_player_index + 1) % 2
            
blue = AI('b')
red = AI('r')
game = Game(blue, red)
game.play()