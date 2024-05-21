import random
import math
from main import generate_gameboard2, get_move_list, switch_char2

class AI:
    def __init__(self, name):
        self.name = name # Farbe
        self.movestack = []
    
    def __init__(self, name):
        self.name = name # Farbe

    def determine_next_move(self):
        _, move = self.alpha_beta_search(game.board, self.name, 3, -math.inf, math.inf, True)
        self.movestack(move)
        return move
    
    def movestack(self, move):
        self.movestack += move
        return

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
        opponent = 'r' if player == 'b' else 'b'
        score = 0

        # Define the value for each type of piece
        single_value = 1
        double_value = 3
        mixed_double_value = 2
        
        # Define the importance of reaching the opponent's back rank
        back_rank_bonus = 100
        capture_bonus = 10

        # Loop through the board to evaluate the positions
        for row in range(len(board)):
            for col in range(len(board[row])):
                piece = board[row][col]
                
                if piece == 'b':
                    score += single_value if player == 'b' else -single_value
                elif piece == 'r':
                    score += single_value if player == 'r' else -single_value
                elif piece == 'bb':
                    score += double_value if player == 'b' else -double_value
                elif piece == 'rr':
                    score += double_value if player == 'r' else -double_value
                elif piece == 'br' or piece == 'rb':
                    score += mixed_double_value if player == 'b' else -mixed_double_value
                
                # Check if a piece has reached the opponent's back rank
                if piece in ['b', 'bb'] and row == len(board) - 1 and player == 'b':
                    score += back_rank_bonus
                elif piece in ['r', 'rr'] and row == 0 and player == 'r':
                    score += back_rank_bonus
        
        # Use get_move_list to get all possible moves for the current player
        possible_moves = get_move_list(board, player)
        
        for move in possible_moves:
            new_board = self.simulate_move(board, move)
            move_score = self.evaluate_board(new_board, player)
            
            # Adjust score based on the future board state
            score += move_score / len(possible_moves)  # Average the potential outcomes

        return score

    def switch_player(self, player):
        return 'b' if player == 'r' else 'r'
    
class Game:
    def __init__(self, p1, p2):
        self.board = generate_gameboard2()
        self.players = [p1, p2]
        self.current_player_index = 0
        
    def make_move(board, move):
        def get_position(pos):
            x = switch_char2(pos[0])
            y = int(pos[1]) - 1
            return x, y

        start_pos, end_pos = move.split('-')
        start_x, start_y = get_position(start_pos)
        end_x, end_y = get_position(end_pos)
        print(move)

        def update_board(start, end, new_start_val, new_end_val):
            start_x, start_y = start
            end_x, end_y = end
            board[end_y][end_x] = new_end_val
            board[start_y][start_x] = new_start_val

        start_val = board[start_y][start_x]
        end_val = board[end_y][end_x]

        if end_val == '':
            if start_val == 'b' or start_val == 'r':
                update_board((start_x, start_y), (end_x, end_y), '', start_val)
            elif start_val == 'rr' or start_val == 'bb':
                update_board((start_x, start_y), (end_x, end_y), start_val[1], start_val[0])
            elif start_val == 'rb' or start_val == 'br':
                update_board((start_x, start_y), (end_x, end_y), start_val[0], start_val[1])
        else:
            if (start_val, end_val) in [('r', 'r'), ('b', 'b')]:
                update_board((start_x, start_y), (end_x, end_y), '', start_val * 2)
            elif (start_val, end_val) in [('r', 'b'), ('b', 'r')]:
                update_board((start_x, start_y), (end_x, end_y), '', start_val + end_val)
            elif (start_val, end_val) in [('rr', 'b'), ('rb', 'r'), ('br', 'b'), ('bb', 'r')]:
                update_board((start_x, start_y), (end_x, end_y), start_val[1], start_val[0] + end_val)
            elif (start_val, end_val) in [('rr', 'r'), ('br', 'r'), ('bb', 'b'), ('rb', 'b')]:
                update_board((start_x, start_y), (end_x, end_y), start_val[0], start_val + end_val)
            
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
