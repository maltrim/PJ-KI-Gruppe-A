##Zuggenerator
# moves (x,y):
# valid moves red one figure: left, right, down
move_hv_red = [(-1,0), (1,0), (0,-1)]
# valid moves red attack figure: left down, right down
move_diagonal_red = [(-1,-1),(1,-1)]
# valid moves red two figures: 2left+down, left+2down, right+2down, 2right+down
move_two_fgR = [(-2,-1),(-1,-2),(1,-2),(2,-1)]

# valid moves blue one figur: right, left, up
move_hv_blue = [(1,0), (-1,0), (0,1)]
# valid moves blue attack figure: right upper, left upper
move_diagonal_blue = [(1,1),(-1,1)]
# valid moves blue two figures: 2left+up, left+2up, right+2up, 2right+up
move_two_fgB = [(-2,1),(-1,2),(1,2),(2,1)]

def fen_to_available_moves(fen):
    board_str, turn = fen.split(' ')
    
    gameboard = generate_gameboard(board_str)
    
    move_list = get_move_list(gameboard)
    
    # TODO movelist to string ausgabe!, wrong right now, check output
    move_list_str = move_list
    
    return move_list_str

def generate_gameboard(fen):
    gameboard = [[''] * 8 for _ in range(8)]
    
    fen_parts = fen.split('/')
    fen_parts[0] = '1' + fen_parts[0]
    fen_parts[7] = '1' + fen_parts[7]
    
    for row_index, row in enumerate(fen_parts):
        column_index = 0
        for char in row:
            if char.isdigit():
                if int(char) >= 1:
                    column_index += int(char)
                else:
                    column_index += 1
            else:
                if char == 'b':
                    if gameboard[row_index][column_index] == 'b':
                        gameboard[row_index][column_index] = 'bb'
                        column_index += 1
                    elif gameboard[row_index][column_index] == 'r':
                        gameboard[row_index][column_index] = 'rb'
                        column_index += 1
                    else:
                        gameboard[row_index][column_index] = 'b'
                elif char == 'r':
                    if gameboard[row_index][column_index] == 'r':
                        gameboard[row_index][column_index] = 'rr'
                        column_index += 1
                    elif gameboard[row_index][column_index] == 'b':
                        gameboard[row_index][column_index] = 'br'
                        column_index += 1
                    else:
                        gameboard[row_index][column_index] = 'r'
                
    gameboard[0][0] = None
    gameboard[0][7] = None
    gameboard[7][0] = None
    gameboard[7][7] = None
    
    return gameboard

def get_move_list(gameboard):
    list = []
    count = 0
    for y, row in enumerate(gameboard):
        for x, elem in enumerate(row):
            if elem == 'r':
                for move in move_hv_red:
                    if x + move[0] >= 7: # TODO test every possibility
                        count += 1
                        list += get_move(x, y, x+move[0], y+move[1])
                count += 1
                list += []
            elif elem == 'rr':
                count += 0
            elif elem == 'b':
                count += 0
            elif elem == 'bb':
                count += 0
            elif elem == 'br':
                count += 0
            elif elem == 'rb':
                count += 0
        
    return [count] + list
    
def get_move(x, y, x_new, y_new):
    move = switch_char(x) + str(y) +'-'+ switch_char(x_new) + str(y_new)   
    return [move]

def switch_char(x):
    if x==0:
        a='A'
    elif x==1:
        a='B'
    elif x==2:
        a='C'
    elif x==3:
        a='D'
    elif x==4:
        a='E'
    elif x==5:
        a='F'
    elif x==6:
        a='G'
    elif x==7:
        a='H'
    return a
    
    
fen_str = 'b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b'
