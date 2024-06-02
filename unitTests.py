import unittest
import math
from unittest.mock import patch
from main import *
from game import *

class TestMain(unittest.TestCase):

    def test_fen_to_available_moves(self):
        fen_str = 'b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 r'
        expected = '34 Züge: B7-A7, B7-C7, B7-B6, C7-B7, C7-D7, C7-C6, D7-C7, D7-E7, D7-D6, E7-D7, E7-F7, E7-E6, F7-E7, F7-G7, F7-F6, G7-F7, G7-H7, G7-G6, B8-C8, B8-B7, C8-B8, C8-D8, C8-C7, D8-C8, D8-E8, D8-D7, E8-D8, E8-F8, E8-E7, F8-E8, F8-G8, F8-F7, G8-F8, G8-G7'
        self.assertEqual(fen_to_available_moves(fen_str), expected)
 
    def test_generate_gameboard(self):
        fen_str = 'b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 r'
        expected_gameboard = [
            [None, 'b', 'b', 'b', 'b', 'b', 'b', None],
            ['', 'b', 'b', 'b', 'b', 'b', 'b', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
            ['', 'r', 'r', 'r', 'r', 'r', 'r', ''],
            [None, 'r', 'r', 'r', 'r', 'r', 'r', None]
            ]     
        self.assertEqual(generate_gameboard(fen_str), expected_gameboard)

    def test_get_move_list(self):
        gameboard =[
            [None, 'b', 'b', 'b', 'b', 'b', 'b', None],
            ['', 'b', 'b', 'b', 'b', 'b', 'b', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
            ['', 'r', 'r', 'r', 'r', 'r', 'r', ''],
            [None, 'r', 'r', 'r', 'r', 'r', 'r', None]
            ]     
        tested = set(get_move_list(gameboard, 'r'))
        expected = {34,'B7-A7','B7-C7','B7-B6','C7-B7','C7-D7','C7-C6','D7-C7','D7-E7','D7-D6','E7-D7','E7-F7','E7-E6','F7-E7','F7-G7','F7-F6','G7-F7','G7-H7','G7-G6','B8-C8','B8-B7','C8-B8','C8-D8','C8-C7','D8-C8','D8-E8','D8-D7','E8-D8','E8-F8','E8-E7','F8-E8','F8-G8','F8-F7','G8-F8','G8-G7'}
        self.assertEqual(tested, expected)

    def test_get_move(self):
        expected = ['D6-B7']
        self.assertEqual(get_move(3,5,1,6),expected)
    
    def test_is_game_over(self):
        gameboard =[
            [None, '', '', '', '', '', '', None],
            ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', 'b', 'bb', '', '', ''],
                ['', 'r', '', '', '', '', '', ''],
            ['', 'b', '', '', '', 'rr', '', ''],
            [None, '', '', '', 'r', '', '', None]
            ]    
        expected = True
    
    def test_alpha_beta_search(self, mock_get_move_list, mock_evaluate_board):
        mock_evaluate_board.side_effect = lambda board, player: 1 if player == 'X' else -1
        mock_get_move_list.side_effect = lambda board, player: [3, 'move1', 'move2'] if player == 'X' else [3, 'move3', 'move4']

        board =[
            [None, '', '', '', '', '', '', None],
            ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', 'b', 'bb', '', '', ''],
                ['', 'r', '', '', '', '', '', ''],
            ['', 'b', '', '', '', 'rr', '', ''],
            [None, '', '', '', 'r', '', '', None]
            ]    

        score, move = self.ai.alpha_beta_search(board, 'X', 3, 3, -math.inf, math.inf, 1)
        
        self.assertEqual(score, 1)
        self.assertIn(move, ['move1', 'move2'])

    def test_alpha_beta_search_game_over(self, mock_get_move_list, mock_evaluate_board):
        mock_evaluate_board.side_effect = lambda board, player: 1 if player == 'X' else -1
        mock_get_move_list.side_effect = lambda board, player: [0]  # No moves, game over

        board =[
            [None, '', '', '', 'b', 'b', 'b', None],
            ['', '', '', '', '', '', '', ''],
                ['', 'rr', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', 'b', 'bb', '', '', ''],
                ['', 'r', '', '', '', '', '', ''],
            ['', '', '', '', '', 'rr', '', ''],
            [None, 'r', '', '', 'r', '', '', None]
            ]    

        with patch.object(game, 'is_game_over', return_value=True):
            score, move = self.ai.alpha_beta_search(board, 'X', 3, 3, -math.inf, math.inf, 1)
        
        # Validate the results
        self.assertEqual(score, 1)
        self.assertIsNone(move)

    def test_alpha_beta_search_with_depth_zero(self, mock_get_move_list, mock_evaluate_board):
        # Mock the functions
        mock_evaluate_board.side_effect = lambda board, player: 1 if player == 'X' else -1
        mock_get_move_list.side_effect = lambda board, player: [3, 'move1', 'move2']

        board =[
            [None, '', '', '', '', 'b', 'b', None],
            ['', '', '', '', '', '', '', 'b'],
                ['', 'bb', '', '', 'r', 'rr', '', ''],
                ['', 'r', '', '', '', '', '', ''],
                ['', 'b', '', 'b', 'bb', '', '', ''],
                ['', 'r', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            [None, 'r', '', '', 'r', '', '', None]
            ]    

        # Call alpha_beta_search with depth 0
        score, move = self.ai.alpha_beta_search(board, 'X', 0, 3, -math.inf, math.inf, 1)
        
        # Validate the results
        self.assertEqual(score, 1)
        self.assertIsNone(move)
        
obj = TestMain()
print(obj.test_fen_to_available_moves())
print(obj.test_generate_gameboard())
print(obj.test_get_move_list())
print(obj.test_get_move())
print(obj.test_is_game_over())

