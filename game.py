import random
from main import generate_gameboard2, get_move_list

class AI:
    def __init__(self, name):
        self.name = name # Farbe
        
    def determine_next_move(self):
        move_list = get_move_list(game.board, self.name)
        print(move_list)
        move_list = move_list.pop(0) # Count entfernen
        print(move_list)
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
        start_x = ord(start_pos[0]) - ord('A')
        start_y = int(start_pos[1]) - 1
        end_x = ord(end_pos[0]) - ord('A')
        end_y = int(end_pos[1]) - 1
    
        # Führe den Zug auf dem Spielbrett aus
        self.board[end_y][end_x] = self.board[start_y][start_x]
        self.board[start_y][start_x] = ''
        
    def is_game_over(self):
        gameboard = self.board
        turn2 = self.players[self.current_player_index]
        print(turn2)
        turn = turn2.name
        
        if turn == 'r':
            opponent = 'b'
            opponent_row = 8
        elif turn == 'b':
            opponent = 'r'
            opponent_row = 1

        # no figures left
        opponent_figures_remaining = any(opponent in row for row in gameboard)
        if not opponent_figures_remaining:
            return True
        
        #no opponents moves left
        opponent_moves_available = any(get_move_list(gameboard, opponent))
        if not opponent_moves_available:
            return True
        
        #reach opponent last row
        for row in gameboard:
            if opponent in row:
                if opponent_row == 1:
                    return True  # Red hat die letzte Reihe von Blue erreicht
                elif opponent_row == 8:
                    return True  # Blue hat die letzte Reihe von Red erreicht
                
        return False
            
    def play(self):
        while not self.is_game_over():
            current_player = self.players[self.current_player_index]
            next_move = current_player.determine_next_move(self)
            self.make_move(next_move)
            self.current_player_index = (self.current_player_index + 1) % 2
            
blue = AI('b')
red = AI('r')
game = Game(blue, red)
game.play