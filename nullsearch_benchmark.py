import time
from game import AI, Game
import math
from main import *

def test_null_move_pruning_execution_time():
    blue = AI('b')
    red = AI('r')
    game = Game(blue, red)

    depth = 4

    # Ohne Nullzug-Suche
    start_time = time.time()
    _ , blue_move, blue_nodes_without_null = blue.alpha_beta_search(game.board, 'b', depth, -math.inf, math.inf, 1, start_time)
    duration_without_null = time.time() - start_time

    # Mit Nullzug-Suche
    start_time = time.time()
    _ , blue_move, blue_nodes_with_null = blue.alpha_beta_search_with_null_move(game.board, 'b', depth, -math.inf, math.inf, 1, start_time)
    duration_with_null = time.time() - start_time

    print(f"Execution time without null move pruning: {duration_without_null:.6f} seconds")
    print(f"Nodes searched without null move pruning: {blue_nodes_without_null}")
    print(f"Execution time with null move pruning: {duration_with_null:.6f} seconds")
    print(f"Nodes searched with null move pruning: {blue_nodes_with_null}")

test_null_move_pruning_execution_time()