import math
import random
import time
from main import generate_gameboard2, get_move_list, switch_char2, switch_player, make_move, evaluate_board

class AI:
    turnB = True

    def __init__(self, name):
        self.name = name  # Farbe
        self.movelist = []
        self.time_limit = 2.0  # Zeitlimit für die Suche in Sekunden
        self.initial_time_limit = 5.0  # Ein initiales Zeitlimit für die gesamte Berechnung

    def determine_next_move_random(self):
        move_list = get_move_list(game.board, self.name)
        move_list.pop(0)
        return random.choice(move_list)

    def determine_next_move_abs(self, max_depth, turn):
        best_move = None
        best_score = -math.inf
        total_nodes_searched = 0
        total_start_time = time.time()
        remaining_time = self.initial_time_limit

        for depth in range(1, max_depth + 1):
            start_time = time.time()
            # Berechne das Zeitlimit für die aktuelle Tiefe
            depth_time_limit = remaining_time / (max_depth - depth + 1)
            self.time_limit = depth_time_limit

            score, move, nodes = self.alpha_beta_search(game.board, turn, depth, -math.inf, math.inf, 1 if self.turnB else -1, total_start_time)
            #score, move, nodes = self.negaMax(game.board, turn, depth, 1 if self.turnB else -1, total_start_time)
            #score, move, nodes = self.minimax_search(game.board, turn, depth, self.turnB, total_start_time)
            total_nodes_searched += nodes
            duration = time.time() - start_time
            remaining_time -= duration

            if score > best_score:
                best_score = score
                best_move = move

            print(f"Depth: {depth}, Best Score: {best_score}, Best Move: {best_move}, Nodes Searched: {total_nodes_searched}, Time: {duration}s")

            if remaining_time <= 0:
                break

        if len(self.movelist) > 2 and self.movelist[-2] == best_move:
            valid_moves = get_move_list(game.board, turn)
            valid_moves.pop(0)
            best_move = random.choice(valid_moves)

        self.movelist.append(best_move)
        return best_move, total_nodes_searched

    def minimax_search(self, board, player, depth, maximizing_player, start_time):
        nodes_searched = 1
        if time.time() - start_time >= self.time_limit or depth == 0 or game.is_game_over():
            return evaluate_board(board, player), None, nodes_searched

        valid_moves = get_move_list(board, player)
        if not valid_moves or len(valid_moves) == 1:
            return evaluate_board(board, player), None, nodes_searched

        valid_moves.pop(0)  # Remove the count
        best_move = None
        ordered_moves = None
        ordered_moves = self.order_moves(board, valid_moves, player)

        if maximizing_player:
            max_eval = -math.inf
            for move in ordered_moves:
                new_board = self.simulate_move(board, move)
                eval, _ , nodes = self.minimax_search(new_board, switch_player(player), depth - 1, False, start_time)
                nodes_searched += nodes
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            return max_eval, best_move, nodes_searched
        else:
            min_eval = math.inf
            for move in ordered_moves:
                new_board = self.simulate_move(board, move)
                eval, _ , nodes = self.minimax_search(new_board, switch_player(player), depth - 1, True, start_time)
                nodes_searched += nodes
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval, best_move, nodes_searched

    def alpha_beta_search(self, board, player, depth, alpha, beta, maximizing_player, start_time):
        nodes_searched = 1
        if time.time() - start_time >= self.time_limit or depth == 0 or game.is_game_over():
            return evaluate_board(board, player) * maximizing_player, None, nodes_searched

        valid_moves = get_move_list(board, player)
        if not valid_moves or len(valid_moves) == 1:
            return evaluate_board(board, player), None, nodes_searched

        valid_moves.pop(0)  # Remove the count
        best_move = None
        ordered_moves = None
        ordered_moves = self.order_moves(board, valid_moves, player)

        if maximizing_player == 1:
            max_eval = -math.inf
            for move in ordered_moves:
                new_board = self.simulate_move(board, move)
                eval, _ , nodes = self.alpha_beta_search(new_board, switch_player(player), depth - 1, alpha, beta, -maximizing_player, start_time)
                nodes_searched += nodes
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break  # alpha-beta cutoff
            return max_eval, best_move, nodes_searched
        else:
            min_eval = math.inf
            for move in ordered_moves:
                new_board = self.simulate_move(board, move)
                eval, _ , nodes = self.alpha_beta_search(new_board, switch_player(player), depth - 1, alpha, beta, -maximizing_player, start_time)
                nodes_searched += nodes
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if alpha >= beta:
                    break  # alpha-beta cutoff
            return min_eval, best_move, nodes_searched

    def simulate_move(self, board, move):
        new_board = [row[:] for row in board]  # Create a copy of the board
        new_board = make_move(new_board, move)
        return new_board
    
    def order_moves(self, board, moves, player):
        move_scores = []

        for move in moves:
            new_board = self.simulate_move(board, move)
            move_score = evaluate_board(new_board, player)
            move_scores.append((move_score, move))

        # Sort moves based on their heuristic score in descending order
        move_scores.sort(reverse=True, key=lambda x: x[0])
        ordered_moves = [move for _, move in move_scores]

        return ordered_moves
    
    def negaMax(self, board, player, depth, maximizing_player, start_time):
        nodes_searched = 1
        if time.time() - start_time >= self.time_limit or depth == 0 or game.is_game_over():
            return evaluate_board(board, player) * maximizing_player, None, nodes_searched
        
        valid_moves = get_move_list(board, player)
        if not valid_moves or len(valid_moves) == 1:
            return evaluate_board(board, player), None, nodes_searched
        
        valid_moves.pop(0)  # Remove the count
        best_move = None
        ordered_moves = None
        ordered_moves = self.order_moves(board, valid_moves, player)

        max_eval = -math.inf
        for move in ordered_moves:
            new_board = self.simulate_move(board, move)
            eval, _ , nodes = self.negaMax(new_board, switch_player(player), depth - 1, -maximizing_player, start_time)
            nodes_searched += nodes
            eval = -eval  # Negate the evaluation after the recursion for NegaMax
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move, nodes_searched


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
            next_move, _ = current_player.determine_next_move_nm(4, current_player.name)  # hier minimax, alpha beta oder random auswählen
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
