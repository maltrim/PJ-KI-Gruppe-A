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


def switch_char2(x):
    return ord(x.upper()) - ord('A')

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

#bei Spielende return true
#mögliche wins:
#1. Wenn alle gegnerischen Figuren besiegt sind.
#2. Wenn der Gegner am Zug ist und alle seine Figuren blockiert sin bzw. sich nicht mehr bewegen können.
#3. Wenn die Figur eines der 6 hinteren Felder des Gegners erreicht.
#Blue muss dafür Row 8 erreichen
#Red muss dafür Row 1 erreichen 
def spielende(fen):
    board_str, turn = fen.split(' ')
    gameboard = generate_gameboard(board_str)
    
    if turn == 'r':
        opponent = 'b'
        opponent_row = 8
    elif turn == 'b':
        opponent = 'r'
        opponent_row = 1

    # no figures left
    opponent_figures_remaining = any(opponent in row for row in gameboard)
    if not opponent_figures_remaining:
        return True
    
    #no opponents moves left
    opponent_moves_available = any(get_move_list(gameboard, opponent))
    if not opponent_moves_available:
        return True
    
    #reach opponent last row
    for row in gameboard:
        if opponent in row:
            if opponent_row == 1:
                return True  # Red hat die letzte Reihe von Blue erreicht
            elif opponent_row == 8:
                return True  # Blue hat die letzte Reihe von Red erreicht

    return False
    
#fen_str = '6/1b0b0b0b0b0b01/1b0b0b0b0b0b01/8/8/1r0r0r0r0r0r01/1r0r0r0r0r0r01/6 b'
#print(fen_to_available_moves(fen_str))
#print(determine_next_move(fen_str))
#print(spielende(fen_str))

def generate_gameboard2():
    fen = 'b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 r'
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

def make_move(board, move):
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
            
    return board

def evaluate_board(board, player):
    opponent = 'r' if player == 'b' else 'b'
    score = 0

    # Define the value for each type of piece
    single_value = 1
    double_value = 3
    mixed_double_value = 2
    
    # Define the importance of reaching the opponent's back rank
    back_rank_bonus = 100
    one_back_bevor_bonus = 50
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
            if piece in ['b', 'bb', 'rb'] and row == len(board) - 1 and player == 'b':
                score += back_rank_bonus
            elif piece in ['r', 'rr', 'br'] and row == 0 and player == 'r':
                score += back_rank_bonus

            if piece in ['b', 'bb', 'rb'] and row == len(board) - 2 and player == 'b':
                score += one_back_bevor_bonus
            elif piece in ['r', 'rr', 'br'] and row == 1 and player == 'r':
                score += one_back_bevor_bonus

    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]
            if piece in ['b', 'bb', 'rb'] and player == 'b':
                # Check for captures by 'b' player
                if (row > 1 and col > 1 and board[row-1][col-1] in ['r', 'rr', 'br'] and board[row-2][col-2] == 'e') or \
                   (row > 1 and col < len(board[row]) - 2 and board[row-1][col+1] in ['r', 'rr', 'br'] and board[row-2][col+2] == 'e'):
                    score += capture_bonus
            elif piece in ['r', 'rr', 'br'] and player == 'r':
                # Check for captures by 'r' player
                if (row < len(board) - 2 and col > 1 and board[row+1][col-1] in ['b', 'bb', 'rb'] and board[row+2][col-2] == 'e') or \
                   (row < len(board) - 2 and col < len(board[row]) - 2 and board[row+1][col+1] in ['b', 'bb', 'rb'] and board[row+2][col+2] == 'e'):
                    score += capture_bonus
    # Use get_move_list to get all possible moves for the current player
    #possible_moves = get_move_list(board, player)
    #
    #for move in possible_moves:
    #    new_board = make_move(board, move)
    #    move_score = evaluate_board(new_board, player)
    #    
    #    # Adjust score based on the future board state
    #    score += move_score / len(possible_moves)  # Average the potential outcomes

    return score

def count_pieces(board, turn):
    count = 0
    for row in board:
        for cell in row:
            if turn in cell:
                count += 1
    return count

def switch_player(player):
    return 'b' if player == 'r' else 'r'