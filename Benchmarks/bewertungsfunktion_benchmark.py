import time
from Game.game_xd import AI, Game
from main import generate_gameboard, get_move_list, evaluate_board

fen_str_start = 'b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b'
fen_str_mid = 'b01bbb01b0/1b02b03/3bbr01b01/8/3rr1b0b01/8/2r01r01rr1/r0r0r01r01 r'
fen_str_end = '2b02bb/1bb2b03/5bb2/8/1r03r02/6r01/8/r01r01rrr0 b'

def main():
    objB = AI('b')
    objR = AI('r')
    objGame = Game(objB, objR)

    execution_times = []

    execution_times_start = []

    objGame.board = generate_gameboard(fen_str_start)

    for _ in range(1000):
        start_time = time.time()
        score = evaluate_board(objGame.board, 'b')
        end_time = time.time()
        execution_time_start = end_time - start_time
        execution_times_start.append(execution_time_start)

    average_execution_time_start = sum(execution_times_start) / len(execution_times_start)
    execution_times.append(average_execution_time_start)

    execution_times_mid = []

    objGame.board = generate_gameboard(fen_str_mid)

    for _ in range(1000):
        start_time = time.time()
        score = evaluate_board(objGame.board, 'r')
        end_time = time.time()
        execution_time_mid = end_time - start_time
        execution_times_mid.append(execution_time_mid)

    average_execution_time_mid = sum(execution_times_mid) / len(execution_times_mid)
    execution_times.append(average_execution_time_mid)

    execution_times_end = []

    objGame.board = generate_gameboard(fen_str_end)

    for _ in range(1000):
        start_time = time.time()
        score = evaluate_board(objGame.board, 'b')
        end_time = time.time()
        execution_time_end = end_time - start_time
        execution_times_end.append(execution_time_end)

    average_execution_time_end = sum(execution_times_end) / len(execution_times_end)
    execution_times.append(average_execution_time_end)


    return execution_times

t = main()
print(t)