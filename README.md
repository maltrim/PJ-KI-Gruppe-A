### PJ-KI-Gruppe-A
### Bedienungsanleitung
## Auszuführende Klasse `game.py` 
## Darin befinden sich die Klassen `AI` und `Game`
# Class AI
In der Klasse befindet sich die Funktion `detemine_next_move()`.
Darin kann man eines der folgenden Suchalgorithmen ausführen:
- Min-Max-Suche: `minimax_search()` 
- Alpha-Beta-Suche: `alpha_beta_search` 
- Alpha-Beta-Suche mit Nullzugsuche: `alpha_beta_search_with_null_move`
- NegaMax-Suche: `negaMax()`

In der Funktion `detemine_next_move_random()` wird der Zuggenerator `get_move_list()` aufgerufen.
Der Zuggenerator: Checkt alle möglichen Züge eines gegebenes FEN-Strings bzw. einer Spielsituation.

# Class Game
In der Klasse `Game` kann man in der Funktion `play` die Tiefe festlegen.
Die Spieler (die AI's) werden initialisiert und deklariert mit der Zuweisung rot(`r`) und blau (`b`) und anschließend das Spiel gestartet.
`blue = AI('b')`
`red = AI('r')`
`game = Game(blue, red)`
`game.play()` Momentan auskommentiert, aufgrund der Benchmarks. Bitte # entfernen, um MCTS vs. Alpha-Beta spielen zu lassen.