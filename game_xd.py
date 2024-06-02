import math
import random
import time
from main import generate_gameboard2, get_move_list, switch_char2, switch_player, make_move, evaluate_board

class AI:
    def __init__(self, name):
        self.name = name  # Farbe
        self.movelist = []
        self.time_limit = 5.0  # Zeitlimit für die Suche in Sekunden

    def determine_next_move(self):
        best_move = None
        best_score = -math.inf
        start_time = time.time()
        depth = 1

        # If no move is found, use random move
        move_list = get_move_list(game.board, self.name)
        move_list.pop(0)
        move = random.choice(move_list)
        
        while time.time() - start_time < self.time_limit:
            score, move = self.alpha_beta_search(game.board, self.name, depth, -math.inf, math.inf, True, start_time)
            if time.time() - start_time >= self.time_limit:
                break
            if score > best_score:
                best_score = score
                best_move = move
            depth += 1

        self.movelist.append(best_move)
        return best_move

    def alpha_beta_search(self, board, player, depth, alpha, beta, maximizing_player, start_time):
        if time.time() - start_time >= self.time_limit or depth == 0 or game.is_game_over():
            return evaluate_board(board, player), None

        valid_moves = get_move_list(board, player)
        if not valid_moves:
            return evaluate_board(board, player), None

        valid_moves.pop(0)  # Remove the count
        best_move = None

        if maximizing_player:
            max_eval = -math.inf
            for move in valid_moves:
                new_board = self.simulate_move(board, move)
                eval, _ = self.alpha_beta_search(new_board, switch_player(player), depth - 1, alpha, beta, False, start_time)
                if eval > max_eval:
                    max_eval = eval
                    if depth == 1:  # Save best move only at the first depth level
                        best_move = move
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break  # cutoff
            return max_eval, best_move
        else:
            min_eval = math.inf
            for move in valid_moves:
                new_board = self.simulate_move(board, move)
                eval, _ = self.alpha_beta_search(new_board, switch_player(player), depth - 1, alpha, beta, True, start_time)
                if eval < min_eval:
                    min_eval = eval
                    if depth == 1:  # Save best move only at the first depth level
                        best_move = move
                beta = min(beta, eval)
                if alpha >= beta:
                    break  # cutoff
            return min_eval, best_move

    def simulate_move(self, board, move):
        new_board = [row[:] for row in board]  # Create a copy of the board
        new_board = make_move(new_board, move)
        return new_board

    def undo_move(self):
        if not self.movelist:
            return  # No move to undo

        start, start_cell, end, end_cell = self.movelist.pop()
        start_row, start_col = int(start[1]) - 1, ord(start[0]) - 65
        end_row, end_col = int(end[1]) - 1, ord(end[0]) - 65
        game.board[start_row][start_col] = start_cell
        game.board[end_row][end_col] = end_cell

class Game:
    def __init__(self, p1, p2):
        self.board = generate_gameboard2()
        self.players = [p1, p2]
        self.current_player_index = 0

    def make_move(self, move):
        if move is None:
            print(f"Player {self.players[self.current_player_index].name} has no valid moves. Game over.")
            return

        def get_position(pos):
            x = switch_char2(pos[0])
            y = int(pos[1]) - 1
            return x, y

        start_pos, end_pos = move.split('-')
        start_x, start_y = get_position(start_pos)
        end_x, end_y = get_position(end_pos)

        def update_board(start, end, new_start_val, new_end_val):
            start_x, start_y = start
            end_x, end_y = end
            self.board[end_y][end_x] = new_end_val
            self.board[start_y][start_x] = new_start_val

        start_val = self.board[start_y][start_x]
        end_val = self.board[end_y][end_x]

        if end_val == '':
            if start_val == 'b' or start_val == 'r':
                update_board((start_x, start_y), (end_x, end_y), '', start_val)
            elif start_val in ['br','bb','rb','rr']:
                update_board((start_x, start_y), (end_x, end_y), start_val[0], start_val[1])
        else:
            if (start_val, end_val) in [('r', 'r'), ('b', 'b')]:
                update_board((start_x, start_y), (end_x, end_y), '', start_val * 2)
            elif (start_val, end_val) in [('r', 'b'), ('b', 'r')]:
                update_board((start_x, start_y), (end_x, end_y), '', start_val)
            elif (start_val, end_val) in [('rr', 'b'), ('rb', 'r'), ('br', 'b'), ('bb', 'r')]:
                update_board((start_x, start_y), (end_x, end_y), start_val[0], start_val[1])
            elif (start_val, end_val) in [('rr', 'r'), ('br', 'r'), ('bb', 'b'), ('rb', 'b')]:
                update_board((start_x, start_y), (end_x, end_y), start_val[0], end_val + start_val[1])
            elif (start_val, end_val) in [('b', 'br'), ('r', 'rb'), ('b', 'rr'), ('r', 'bb')]:
                update_board((start_x, start_y), (end_x, end_y), '', end_val[0] + start_val)
            elif (start_val, end_val) in [('bb', 'br'), ('rr', 'rb'), ('br', 'bb'), ('rb', 'rr')]:
                update_board((start_x, start_y), (end_x, end_y), start_val[0], end_val[0] + start_val[1])
            

    def is_game_over(self):
        gameboard = self.board
        turn = self.players[self.current_player_index].name
        count = 0

        if turn == 'r':
            opponents = ['b', 'rb', 'bb']
            own_row = 7
        elif turn == 'b':
            opponents = ['r', 'br', 'rr']
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
            print(next_move)
            self.make_move(next_move)
            if next_move is None:
                break
            self.current_player_index = (self.current_player_index + 1) % 2
            print(self.board)

blue = AI('b')
red = AI('r')
game = Game(blue, red)
game.play()
