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

gameboard = [[''] * 8 for _ in range(8)]

#moves in dictionary
moves = {'r0':[1, *move_diagonal_red],
         'rr':[1, *move_two_fgR],
         'b0':[1, *move_hv_blue],
         'bb':[1, *move_two_fgB]}

#generate reds moves
def zugGen(red,position):
    züge = []
    pseudo = pseudoZugGen(red, position)
    return züge 

def pseudoZugGen(red, position):
    pseudo = []
    for von, fig in position.items():
        if fig.isloser() != red: continue
        if fig in 'r': continue

        richtungen = moves[fig][1:]
        multiplikator = moves[fig][0]
        for ds, dz in richtungen: 
            for m in range(1, multiplikator + 1):
                zu = von[0] + ds * m
                if zu not in gameboard: break
                if zu in position and position[zu].islower() == red: break
                if zu in position and position[zu].islower() != red: break
                pseudo.append((fig, von, zu, position[zu]))
                break
            else:
                pseudo.append((fig, von, zu, False))
        return pseudo 


#generate reds moves
def zugGen(blue,Position):
    züge = []
    return züge 