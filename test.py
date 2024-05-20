import random
import math
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
    
    def __init__(self, name):
        self.name = name # Farbe

    def determine_next_move(self):
        _, move = self.alpha_beta_search(game.board, self.name, 3, -math.inf, math.inf, True)
        return move

    def alpha_beta_search(self, board, player, depth, alpha, beta, maximizing_player):
        if depth == 0 or game.is_game_over():
            return self.evaluate_board(board, player), None

        valid_moves = get_move_list(board, player)
        valid_moves.pop(0) # Remove the count

        if maximizing_player:
            max_eval = -math.inf
            best_move = None
            for move in valid_moves:
                new_board = self.simulate_move(board, move)
                eval, _ = self.alpha_beta_search(new_board, self.switch_player(player), depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = math.inf
            best_move = None
            for move in valid_moves:
                new_board = self.simulate_move(board, move)
                eval, _ = self.alpha_beta_search(new_board, self.switch_player(player), depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def simulate_move(self, board, move):
        # Make a deep copy of the board
        new_board = [row[:] for row in board]
        start_pos, end_pos = move.split('-')
        start_x = switch_char2(start_pos[0])
        start_y = int(start_pos[1]) - 1
        end_x = switch_char2(end_pos[0])
        end_y = int(end_pos[1]) - 1
        new_board[end_y][end_x] = new_board[start_y][start_x]
        new_board[start_y][start_x] = ''
        return new_board

    def evaluate_board(self, board, player):
        # Simple evaluation function: count the number of pieces
        opponent = self.switch_player(player)
        player_pieces = sum(row.count(player) for row in board)
        opponent_pieces = sum(row.count(opponent) for row in board)
        return player_pieces - opponent_pieces

    def switch_player(self, player):
        return 'b' if player == 'r' else 'r'
    
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
        print(move)
        
        # Zielfeld ist frei:
        if (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'b'):
            self.board[end_y][end_x] ='b'
            self.board[start_y][start_x] = ''
            return
        elif (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'r'):
            self.board[end_y][end_x] ='r'
            self.board[start_y][start_x] = ''
            return
        elif (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'rr'):
            self.board[end_y][end_x] ='r'
            self.board[start_y][start_x] = 'r'
            return
        elif (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'bb'):
            self.board[end_y][end_x] ='b'
            self.board[start_y][start_x] = 'b'
            return
        elif (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'rb'):
            self.board[end_y][end_x] ='b'
            self.board[start_y][start_x] = 'r'
            return
        elif (self.board[end_y][end_x] == '' and self.board[start_y][start_x] == 'br'):
            self.board[end_y][end_x] ='r'
            self.board[start_y][start_x] = 'b'
            return
            
        # Zielfeld hat ein Stein:
        if (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'r'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = ''
            return
        elif (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'b'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = ''
            return
        elif (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'br'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = 'b'
            return
        elif (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'rb'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = 'r'
            return
        elif (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'bb'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = 'b'
            return
        elif (self.board[end_y][end_x] == 'r' and self.board[start_y][start_x] == 'rr'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = 'r'
            return
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'r'): # ab hier mit blau als ziel
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = ''
            return
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'b'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = ''
            return
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'rb'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = 'r'
            return
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'br'):
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = 'b'
            return
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'bb'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = 'b'
            return
        elif (self.board[end_y][end_x] == 'b' and self.board[start_y][start_x] == 'rr'):
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = 'r'
            return
            
        # Zielfeld hat zwei Steine:
        if (self.board[end_y][end_x] == 'rr' and self.board[start_y][start_x] == 'b'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = ''
            return
        elif (self.board[end_y][end_x] == 'rr' and self.board[start_y][start_x] == 'bb'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = 'b'
            return
        elif (self.board[end_y][end_x] == 'rr' and self.board[start_y][start_x] == 'rb'):
            self.board[end_y][end_x] ='rb'
            self.board[start_y][start_x] = 'r'
            return
        elif (self.board[end_y][end_x] == 'rb' and self.board[start_y][start_x] == 'r'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = ''
            return
        elif (self.board[end_y][end_x] == 'rb' and self.board[start_y][start_x] == 'rr'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = 'r'
            return
        elif (self.board[end_y][end_x] == 'rb' and self.board[start_y][start_x] == 'br'):
            self.board[end_y][end_x] ='rr'
            self.board[start_y][start_x] = 'b'
            return
        elif (self.board[end_y][end_x] == 'br' and self.board[start_y][start_x] == 'b'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = ''
            return
        elif (self.board[end_y][end_x] == 'br' and self.board[start_y][start_x] == 'bb'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = 'b'
            return
        elif (self.board[end_y][end_x] == 'br' and self.board[start_y][start_x] == 'rb'):
            self.board[end_y][end_x] ='bb'
            self.board[start_y][start_x] = 'r'
            return
        elif (self.board[end_y][end_x] == 'bb' and self.board[start_y][start_x] == 'r'):
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = ''
            return
        elif (self.board[end_y][end_x] == 'bb' and self.board[start_y][start_x] == 'rr'):
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = 'r'
            return
        elif (self.board[end_y][end_x] == 'bb' and self.board[start_y][start_x] == 'br'):
            self.board[end_y][end_x] ='br'
            self.board[start_y][start_x] = 'b'
            return
        
    def is_game_over(self):
        gameboard = self.board
        turn = self.players[self.current_player_index].name
        count = 0
        
        if turn == 'r':
            opponents = ['b','rb','bb']
            own_row = 7
        elif turn == 'b':
            opponents = ['r','br','rr']
            own_row = 0

        # no figures left for all opponents
        for opp in opponents:
            opponent_figures_remaining = any(opp in row for row in gameboard)
            if opponent_figures_remaining:
                count += 1
            
        if count == 0:
            print('Game over, no figures left!')
            return True
        else:
            count = 0

        # no opponents moves left for all opponents
        for opp in opponents:
            opponent_moves_available = any(get_move_list(gameboard, opp))
            if opponent_moves_available:
                count += 1
            
        if count == 0:
            print('Game over, no available moves left!')
            return True
        else:
            count = 0

        # reach opponent last row for all opponents
        for opp in opponents:
            for row_index, row in enumerate(gameboard):
                if opp in row and row_index == own_row:
                    print('Game over, reached the end!')
                    return True
                
        return False


            
    def play(self):
        while not self.is_game_over():
            current_player = self.players[self.current_player_index]
            next_move = current_player.determine_next_move()
            print(current_player.name)
            self.make_move(next_move)
            self.current_player_index = (self.current_player_index + 1) % 2
            print(self.board)
            
blue = AI('b')
red = AI('r')
game = Game(blue, red)
game.play()
