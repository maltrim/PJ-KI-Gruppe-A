import random

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
    
    move_list = get_move_list(gameboard, turn)
    # Count valid moves based on the current turn
    if turn == 'r':
        moves = get_move_list(gameboard, 'r')
    elif turn == 'b':
        moves = get_move_list(gameboard, 'b')
    else:
        moves = []

    # Format output
    output = f"{len(moves)} Züge: "


    move_list_str = ''
    move_list_str += str(move_list[0]) + ' Züge: '
    for i, elem in enumerate(move_list):
        if i == 0:
            continue
        else:
            move_list_str += str(elem) + ', ' 

    return move_list_str [:-2]

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

def get_move_list(gameboard, turn):
    move_list = []
    count = 0
    for y, row in enumerate(gameboard):
        for x, elem in enumerate(row):
            if turn == 'r':
                if elem == 'r':  # Für rote Figuren
                # Horizontale und vertikale Bewegungen
                    for move in move_hv_red:
                        new_x, new_y = x + move[0], y + move[1]
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == '':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'r':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                    # Diagonale Bewegungen für Angriffe
                    for move in move_diagonal_red:
                        new_x, new_y = x + move[0], y + move[1]
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'b':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'bb':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)    
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'rb':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                elif elem == 'rr':
                    for move in move_two_fgR:
                        new_x, new_y = x + move[0], y + move[1]
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == '':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'b':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'bb':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'rb':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                            count += 1
                elif elem == 'br':
                    for move in move_two_fgB:
                        new_x, new_y = x + move[0], y + move[1]
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == '':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'r':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'b':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)        
            if turn == 'b':
                if elem == 'b':
                    # Horizontale und vertikale Bewegungen
                    for move in move_hv_blue:
                        new_x, new_y = x + move[0], y + move[1]
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == '':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'b':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                    # Diagonale Bewegungen für Angriffe
                    for move in move_diagonal_blue:
                        new_x, new_y = x + move[0], y + move[1]
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'r':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'rr':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'br':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                elif elem == 'bb':
                    for move in move_two_fgB:
                        new_x, new_y = x + move[0], y + move[1]
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == '':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'r':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'rr':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'br':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)  
                elif elem == 'rb':
                    for move in move_two_fgB:
                        new_x, new_y = x + move[0], y + move[1]
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == '':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'r':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                        if 0 <= new_x < 8 and 0 <= new_y < 8 and gameboard[new_y][new_x] == 'b':
                            count += 1
                            move_list += get_move(x, y, new_x, new_y)
                    
            
    return [count] + move_list

    
def get_move(x, y, x_new, y_new):
    move = switch_char(x) + str(y+1) +'-'+ switch_char(x_new) + str(y_new+1)   
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

def get_turn(fen):
    board_str, turn = fen.split(' ')
    if turn == 'b':
        return 'b'
    else:
        return 'r'

def determine_next_move(fen):
    gameboard = generate_gameboard(fen)
    turn = get_turn(fen)
    move_list = get_move_list(gameboard, turn)
    move_list = move_list.pop(0)
    return random.choice(move_list)
    
fen_str = '6/1b0b0b0b0b0b01/1b0b0b0b0b0b01/8/8/1r0r0r0r0r0r01/1r0r0r0r0r0r01/6 b'
print(fen_to_available_moves(fen_str))
print(determine_next_move(fen_str)
