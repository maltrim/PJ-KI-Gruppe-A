import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_fen_to_available_moves(self):
        fen_str = 'b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 r'
        expected = '34 Züge: B7-A7, B7-C7, B7-B6, C7-B7, C7-D7, C7-C6, D7-C7, D7-E7, D7-D6, E7-D7, E7-F7, E7-E6, F7-E7, F7-G7, F7-F6, G7-F7, G7-H7, G7-G6, B8-C8, B8-B7, C8-B8, C8-D8, C8-C7, D8-C8, D8-E8, D8-D7, E8-D8, E8-F8, E8-E7, F8-E8, F8-G8, F8-F7, G8-F8, G8-G7'
        self.assertEqual(fen_to_available_moves(fen_str), expected)
 
    def test_generate_gameboard(self):
        fen_str = 'b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 r'
        expected_gameboard = [
            [None, 'r', 'r', 'r', 'r', 'r', 'r', None],
            ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            [None, 'b', 'b', 'b', 'b', 'b', 'b', None]
            ]     
        self.assertEqual(generate_gameboard(fen_str), expected_gameboard)

    def test_get_move_list(self):
        gameboard =[
            [None, 'r', 'r', 'r', 'r', 'r', 'r', None],
            ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
            ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
            [None, 'b', 'b', 'b', 'b', 'b', 'b', None]
            ]     
        expected = ['34 Züge: ','B7-A7','B7-C7','B7-B6','C7-B7','C7-D7','C7-C6','D7-C7','D7-E7','D7-D6','E7-D7','E7-F7','E7-E6','F7-E7','F7-G7','F7-F6','G7-F7','G7-H7','G7-G6','B8-C8','B8-B7','C8-B8','C8-D8','C8-C7','D8-C8','D8-E8','D8-D7','E8-D8','E8-F8','E8-E7','F8-E8','F8-G8','F8-F7','G8-F8','G8-G7']
        self.assertEqual(get_move_list(gameboard, 'b'), expected)

    #def test_get_move(self):
    #    move = switch_char(x) + str(y+1) +'-'+ switch_char(x_new) + str(y_new+1)




    