import unittest
from src.game.gameoflife import *

class GameOfLifeTests(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_dead_cell_zero_neighbors(self):
    testCell = get_next_state(current_state = Cell.Dead, number_of_live_neighbors = 0) 

    self.assertEqual(Cell.Dead, testCell)

  def test_dead_cell_one_neighbors(self):
    testCell = get_next_state(current_state = Cell.Dead, number_of_live_neighbors = 1)

    self.assertEqual(Cell.Dead, testCell)

  def test_dead_cell_two_neighbors(self):
    testCell = get_next_state(current_state = Cell.Dead, number_of_live_neighbors = 2)

    self.assertEqual(Cell.Dead, testCell)

  def test_dead_cell_five_neighbors(self):
    testCell = get_next_state(current_state = Cell.Dead, number_of_live_neighbors = 5)

    self.assertEqual(Cell.Dead, testCell)

  def test_dead_cell_eight_neighbors(self):
    testCell = get_next_state(current_state = Cell.Dead, number_of_live_neighbors = 8)

    self.assertEqual(Cell.Dead, testCell)

  def test_dead_cell_three_neighbors(self):
    testCell = get_next_state(current_state = Cell.Dead, number_of_live_neighbors = 3)

    self.assertEqual(Cell.Alive, testCell)

  def test_alive_cell_one_neighbors(self):
    testCell = get_next_state(current_state = Cell.Alive, number_of_live_neighbors = 1)

    self.assertEqual(Cell.Dead, testCell)

  def test_alive_cell_four_neighbors(self):
    testCell = get_next_state(current_state = Cell.Alive, number_of_live_neighbors = 4)

    self.assertEqual(Cell.Dead, testCell)

  def test_alive_cell_eight_neighbors(self):
    testCell = get_next_state(current_state = Cell.Alive, number_of_live_neighbors = 8)

    self.assertEqual(Cell.Dead, testCell)

  def test_alive_cell_two_neighbors(self):
    testCell = get_next_state(current_state = Cell.Alive, number_of_live_neighbors = 2)

    self.assertEqual(Cell.Alive, testCell)

  def test_alive_cell_three_neighbors(self):
    testCell = get_next_state(current_state = Cell.Alive, number_of_live_neighbors = 3)

    self.assertEqual(Cell.Alive, testCell)

  def test_generate_signals_for_cell_two_three(self):
    expected_result = [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)]
    neighbors = generate_signals((2, 3))

    self.assertEqual(neighbors, expected_result)

  def test_generate_signals_for_cell_three_three(self):
    expected_result = [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
    neighbors = generate_signals((3, 3))

    self.assertEqual(neighbors, expected_result)

  def test_generate_signals_for_cell_two_four(self):
    expected_result = [(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)]
    neighbors = generate_signals((2, 4))

    self.assertEqual(neighbors, expected_result)

  def test_generate_signals_for_cell_zero_zero(self):
    expected_result = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = generate_signals((0, 0))

    self.assertEqual(neighbors, expected_result)

  def test_gen_signals_for_pos_none(self):
    result = generate_signals_for_positions([])

    self.assertTrue(type(result) is list and len(result) is 0)
  
  def test_gen_signals_for_pos_one(self):
    result = generate_signals_for_positions([(0, 0)])

    self.assertTrue(len(result) is 8)

  def test_gen_signals_for_pos_two(self):
    result = generate_signals_for_positions([(0, 0), (1, 1)])

    self.assertTrue(len(result) is 16)

  def test_gen_signals_for_pos_three(self):
    result = generate_signals_for_positions([(0, 0), (1, 1), (2, 2)])

    self.assertTrue(len(result) is 24)

  def test_count_signals_for_position_none(self):
    result = count_signals([])

    self.assertEqual(0, len(result))

  def test_count_signals_for_position_one(self):
    result = count_signals([(0, 0)])

    self.assertTrue(result[(0, 0)] is 1)

  def test_count_signals_for_position_two(self):
    result = count_signals([(1, 1), (1, 1)])

    self.assertTrue(result[(1, 1)] is 2)

  def test_count_signals_for_position_three(self):
    result = count_signals([(1, 1), (3, 3), (1, 1)])

    self.assertTrue(result[(1, 1)] is 2 and result[(3, 3)] is 1)

  def test_next_generation_for_position_none(self):
    result = next_generation([])

    self.assertTrue(type(result) is list and len(result) is 0)

  def test_next_generation_for_position_one(self):
    result = next_generation([(0, 0)])

    self.assertTrue(type(result) is list and len(result) is 0)

  def test_next_generation_for_position_two(self):
    result = next_generation([(2, 3), (2, 4)])

    self.assertTrue(type(result) is list and len(result) is 0)

  def test_next_generation_for_position_three_return_one_position(self):
    result = next_generation([(1, 1), (1, 2), (3, 0)])

    self.assertTrue(result == [(2, 1)])

  def test_next_generation_for_position_three_return_four_positions(self):
    expected_result = [(1, 1), (1, 2), (2, 1), (2, 2)]
    result = next_generation([(1, 1), (1, 2), (2, 2)])

    self.assertTrue(len(result) is len(expected_result) and all([cell in expected_result for cell in result]))

  def test_next_generation_block(self):
    block = [(2, 2), (2, 3), (3, 2), (3, 3)]
    result = next_generation(block)

    self.assertTrue(len(result) is len(block) and all([cell in block for cell in result]))

  def test_next_generation_beehive(self):
    beehive = [(1, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 3)]
    result = next_generation(beehive)

    self.assertTrue(len(result) is len(beehive) and all([cell in beehive for cell in result]))

  def test_next_generation_horizontal_blinker(self):
    horizontal = [(2, 2), (2, 3), (2, 4)]
    vertical  = [(1, 3), (2, 3), (3, 3)]
    result = next_generation(horizontal)

    self.assertTrue(len(result) is 3 and all([cell in vertical for cell in result]))

  def test_next_generation_vertical_blinker(self):
    vertical  = [(1, 3), (2, 3), (3, 3)]
    horizontal = [(2, 2), (2, 3), (2, 4)]
    result = next_generation(vertical)

    self.assertTrue(len(result) is 3 and all([cell in horizontal for cell in result]))

  def test_glider_with_top_cell_moves_right(self):
    glider = [(1, 3), (2, 2), (3, 2), (3, 3), (3, 4)]
    glider2 = [(2, 2), (2, 4), (3, 2), (3, 3), (4, 3)]
    result = next_generation(glider)

    self.assertTrue(len(result) is len(glider2) and all([cell in glider2 for cell in result]))

  def test_get_bounds_returns_empty_list(self):
    result = get_bounds([])

    self.assertEqual( result, [] )

  def test_get_bounds_given_one_returns_two_same(self):
    result = get_bounds([(1, 2)])

    self.assertEqual( result, [(1, 2), (1, 2)] )

  def test_get_bounds_given_two_returns_two_ordered(self):
    result = get_bounds([(7, 5), (4, 6)])

    self.assertEqual( result, [(4, 6), (7, 5)] )

  def test_get_bounds_given_three_returns_two_ordered(self):
    result = get_bounds([ (16, 11), (12, 6), (13, 2) ])

    self.assertEqual( result, [(12, 2), (16, 11)] )

  def test_get_bounds_given_four_returns_two_ordered(self):
    result = get_bounds([ (17, 25), (14, 3), (50, 12), (1,6) ])

    self.assertEqual( result, [(1, 3), (50, 25)] )

if __name__ == '__main__': 
  unittest.main()
