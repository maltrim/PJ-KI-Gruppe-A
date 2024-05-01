##Zuggenerator
#valid moves red one figure
move_hv_red = [(1,0), (-1,0), (0,1)]
#valid moves red attack figure
move_diagonal_red = [(1,1),(-1,1)]
#valid moves blue two figures
move_two_fgR = [(1,2),(-1,2),(2,1),(-2,1)]

#valid moves blue one figur
move_hv_blue = [(1,0), (-1,0), (0,-1)]
#valid moves blue attack figure
move_diagonal_blue = [(1,-1),(-1,-1)]
#valid moves blue two figures
move_two_fgB = [(1,-2),(-1,-2),(2,-1),(-2,-1)]


def fen_to_board(fen):
    # Split FEN string to get board layout and turn information
    board_str, turn = fen.split(' ')

    # Initialize empty board without corners
    gameboard = [[''] * 8 for _ in range(8)]

    # Mark corners as dead
    gameboard[0][0] = 'X'
    gameboard[0][7] = 'X'
    gameboard[7][0] = 'X'
    gameboard[7][7] = 'X'

    # Convert FEN string to board layout
    row = 0
    col = 0
    for char in board_str:
        if char.isdigit():
            col += int(char)
        elif char == '/':
            row += 1
            col = 0
        else:
            # Skip dead spots
            while gameboard[row][col] == 'X':
                col += 1
            gameboard[row][col] = char
            col += 1

    return gameboard, turn


def print_board(gameboard):
    for row in gameboard:
        print(" ".join(str(cell) if cell else '.' for cell in row))

def count_valid_moves(gameboard, color):
    valid_moves = 0

    # Define moves based on color
    if color == 'r0':
        move_hv = move_hv_red
        move_diagonal = move_diagonal_red
    elif color == 'rr':
        move_two_fg = move_two_fgR
    elif color == 'b0':
        move_hv = move_hv_blue
        move_diagonal = move_diagonal_blue
    elif color == 'bb':
        move_two_fg = move_two_fgB
    else:
        return 0

    # Loop through the board
    for row in range(8):
        for col in range(8):
            piece = gameboard[row][col]
            # Exclude corners from consideration
            if (row == 0 and col == 0) or (row == 0 and col == 7) or (row == 7 and col == 0) or (row == 7 and col == 7):
                continue
            if piece and piece.lower() == color:  # Check if piece exists and matches color
                if piece.isupper():  # Check if piece is single
                    # Count horizontal and vertical moves
                    for dr, dc in move_hv:
                        new_row, new_col = row + dr, col + dc
                        if 0 <= new_row < 8 and 0 <= new_col < 8 and gameboard[new_row][new_col] != 'X' and not gameboard[new_row][new_col] and (new_col != 7 and new_row != 0):
                            valid_moves += 1
                else:  # Check if piece is double
                    # Check if there are two figures on one field
                    if row < 7 and gameboard[row][col].lower() == gameboard[row+1][col].lower():
                        # Count knight-like moves
                        for dr, dc in move_two_fg:
                            new_row, new_col = row + dr, col + dc
                            if 0 <= new_row < 8 and 0 <= new_col < 8 and gameboard[new_row][new_col] != 'X' and not gameboard[new_row][new_col]:
                                valid_moves += 1
                        # Check for diagonal attack moves
                        for dr, dc in move_diagonal:
                            new_row, new_col = row + dr, col + dc
                            if 0 <= new_row < 8 and 0 <= new_col < 8 and gameboard[new_row][new_col] != 'X' and gameboard[new_row][new_col] and gameboard[new_row][new_col].lower() != color:
                                valid_moves += 1
                    else:
                        # Count horizontal and vertical moves
                        for dr, dc in move_hv:
                            new_row, new_col = row + dr, col + dc
                            if 0 <= new_row < 8 and 0 <= new_col < 8 and gameboard[new_row][new_col] != 'X' and not gameboard[new_row][new_col]:
                                valid_moves += 1

    return valid_moves

def fen_to_moves(fen_str):
    # Function to count valid moves for a given color
    def count_valid_moves(gameboard, color):
        valid_moves = []

        # Define moves based on color
        if color == 'r':
            move_hv = move_hv_red
            move_diagonal = move_diagonal_red
            move_two_fg = move_two_fgR
        elif color == 'b':
            move_hv = move_hv_blue
            move_diagonal = move_diagonal_blue
            move_two_fg = move_two_fgB
        else:
            return []

        # Loop through the board
        for row in range(8):
            for col in range(8):
                piece = gameboard[row][col]
                if piece and piece.lower() == color:  # Check if piece exists and matches color
                    if piece.isupper():  # Check if piece is single
                        # Find horizontal and vertical moves
                        for dr, dc in move_hv:
                            new_row, new_col = row + dr, col + dc
                            if 0 <= new_row < 8 and 0 <= new_col < 8 and not gameboard[new_row][new_col]:
                                valid_moves.append((row, col, new_row, new_col))
                    else:  # Check if piece is double
                        # Check if there are two figures on one field
                        if row < 7 and gameboard[row][col].lower() == gameboard[row+1][col].lower():
                            # Find knight-like moves
                            for dr, dc in move_two_fg:
                                new_row, new_col = row + dr, col + dc
                                if 0 <= new_row < 8 and 0 <= new_col < 8 and not gameboard[new_row][new_col]:
                                    valid_moves.append((row, col, new_row, new_col))
                            # Find diagonal attack moves
                            for dr, dc in move_diagonal:
                                new_row, new_col = row + dr, col + dc
                                if 0 <= new_row < 8 and 0 <= new_col < 8 and gameboard[new_row][new_col] and gameboard[new_row][new_col].lower() != color:
                                    valid_moves.append((row, col, new_row, new_col))
                        else:
                            # Find horizontal and vertical moves
                            for dr, dc in move_hv:
                                new_row, new_col = row + dr, col + dc
                                if 0 <= new_row < 8 and 0 <= new_col < 8 and not gameboard[new_row][new_col]:
                                    valid_moves.append((row, col, new_row, new_col))

        return valid_moves

    # Parse FEN string
    gameboard, turn = fen_to_board(fen_str)

    # Count valid moves based on the current turn
    if turn == 'r':
        moves = count_valid_moves(gameboard, 'r')
    elif turn == 'b':
        moves = count_valid_moves(gameboard, 'b')
    else:
        moves = []

    # Format output
    output = f"{len(moves)} Züge: "

    # Append moves
    for move in moves:
        output += f"{chr(65 + move[1])}{move[0] + 1}-{chr(65 + move[3])}{move[2] + 1}, "

    # Remove the last comma and space
    output = output[:-2]

    return output

# Test function
fen_str = 'b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b'
print(fen_to_board(fen_str))
print(fen_to_moves(fen_str))
