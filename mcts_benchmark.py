import time
from game import AI, Game, AI_MCTS  
from main import generate_gameboard

fen_str_start = 'b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b'
fen_str_mid = 'b01bbb01b0/1b02b03/3bbr01b01/8/3rr1b0b01/8/2r01r01rr1/r0r0r01r01 r'
fen_str_end = '2b02bb/1bb2b03/5bb2/8/1r03r02/6r01/8/r01r01rrr0 b'

def benchmark(fen_str, method, depth_or_iterations, turn):
    if method == 'mcts':
        objB = AI_MCTS('b')
        objR = AI_MCTS('r')
        objGame = Game(objB, objR)  # Annahme, dass nur ein Spieler benötigt wird
        objGame.board = generate_gameboard(fen_str)
        start_time = time.time()
        if turn == 'b':
            move = objB.mcts_search(objGame.board, turn, depth_or_iterations)
        else:
            move = objR.mcts_search(objGame.board, turn, depth_or_iterations)
    else:
        objB = AI('b')
        objR = AI('r')
        objGame = Game(objB, objR)
        objGame.board = generate_gameboard(fen_str)
        start_time = time.time()
        if turn == 'b':
            move, nodes_searched = objB.determine_next_move(depth_or_iterations, turn)
        else:
            move, nodes_searched = objR.determine_next_move(depth_or_iterations, turn)
    duration = time.time() - start_time
    return move, duration, nodes_searched if method != 'mcts' else "N/A"

def main():
    positions = [fen_str_start, fen_str_mid, fen_str_end]
    turns = ['b', 'r', 'b']
    depths = [4]  # Tiefen für Alpha-Beta
    iterations = 1000  # Iterationen für MCTS

    for fen_str, turn in zip(positions, turns):
        print(f"\nTesting FEN: {fen_str}")
        # Teste Alpha-Beta-Suche
        for depth in depths:
            move, duration, nodes_searched = benchmark(fen_str, 'alpha_beta', depth, turn)
            print(f"Alpha-Beta - Depth: {depth}, Move: {move}, Duration: {duration:.4f}s, Nodes Searched: {nodes_searched}")
        # Teste MCTS
        move, duration, _ = benchmark(fen_str, 'mcts', iterations, turn)
        print(f"MCTS - Iterations: {iterations}, Move: {move}, Duration: {duration:.4f}s")

if __name__ == "__main__":
    main()
