## Zuggenerator ##

# valid moves red one figure
move_hv_red = [(1,0), (-1,0), (0,1)]
# valid moves red two figures
move_diagonal_red = [(1,1),(-1,1)]

# valid moves blue one figur
move_hv_blue = [(1,0), (-1,0), (0,-1)]
# valid moves blue two figures
move_diagonal_blue = [(1,-1),(-1,-1)]


def board():
    # initialize empty board
    gameboard = [
        [''] * 8 for _ in range(8)
    ]

    # delete corner positions
    gameboard[0][0] = None  # a1
    gameboard[0][7] = None  # h1
    gameboard[7][7] = None  # h8
    gameboard[7][0] = None  # a8

    return gameboard

##TODO##
# split String into Array
fen = ''
split_fen = fen.split('/')[0].split(' ')