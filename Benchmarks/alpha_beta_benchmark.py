import time
from Game.game_xd_2 import AI, Game
from main import generate_gameboard

fen_str_start = 'b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b'
fen_str_mid = 'b01bbb01b0/1b02b03/3bbr01b01/8/3rr1b0b01/8/2r01r01rr1/r0r0r01r01 r'
fen_str_end = '2b02bb/1bb2b03/5bb2/8/1r03r02/6r01/8/r01r01rrr0 b'

def benchmark(fen_str):
    objB = AI('b')
    objR = AI('r')
    objGame = Game(objB, objR)
    objGame.board = generate_gameboard(fen_str)
    objB.time_limit = 10  # Increase the time limit for better depth search

    start_time = time.time()
    move, nodes_searched = objB.determine_next_move_abs()
    duration = time.time() - start_time

    return move, duration, nodes_searched

def main():
    positions = [fen_str_start, fen_str_mid, fen_str_end]
    turns = ['b', 'r', 'b']  # Specify the turn for each FEN string
    depths = [2, 3, 4]
    
    for fen_str, turn in zip(positions, turns):
        print(f"Testing FEN: {fen_str}")
        for depth in depths:
            start_time = time.time()
            move, duration, nodes_searched = benchmark(fen_str)
            print(f"Depth: {depth}, Move: {move}, Duration: {duration}s, Nodes Searched: {nodes_searched}")

if __name__ == "__main__":
    main()
