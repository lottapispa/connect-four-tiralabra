import unittest
from gamestatus import GameStatus


class TestGameStatus(unittest.TestCase):
    """Tests class gamestatus."""

    def setUp(self):
        self.rows = GameStatus().rows
        self.columns = GameStatus().columns

    def test_correct_rack_in_the_beginning(self):
        self.gamestatus = GameStatus()
        self.rack = self.gamestatus.rack
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece_wrong_input_color(self):
        """Tests if function raises value error for wrong input color and that the rack doesn't change."""
        self.gamestatus = GameStatus()
        self.rack = self.gamestatus.rack
        self.assertRaises(ValueError, self.gamestatus.insert_piece, 2, 3, "b")
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece_wrong_input_row(self):
        """Tests if function raises value error for wrong input row and that the rack doesn't change."""
        self.gamestatus = GameStatus()
        self.rack = self.gamestatus.rack
        self.assertRaises(
            ValueError, self.gamestatus.insert_piece, 7, 3, "red")
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece_wrong_input_column(self):
        """Tests if function raises value error for wrong input column and that the rack doesn't change."""
        self.gamestatus = GameStatus()
        self.rack = self.gamestatus.rack
        self.assertRaises(
            ValueError, self.gamestatus.insert_piece, 5, 0, "red")
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece(self):
        """Tests if the rack changes correctly."""
        self.gamestatus = GameStatus()
        self.rack = self.gamestatus.rack
        self.gamestatus.insert_piece(2, 3, "red")
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, "red", 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece_wrong_input_spot_taken(self):
        """Tests if function raises value error for wrong input (spot already taken) and that the rack doesn't change."""
        self.gamestatus = GameStatus()
        self.rack = self.gamestatus.rack
        self.gamestatus.insert_piece(1, 2, "red")
        self.assertRaises(
            ValueError, self.gamestatus.insert_piece, 1, 2, "yellow")
        self.assertEqual(self.rack, [[0, "red", 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_game_over_false(self):
        self.gamestatus = GameStatus()
        self.rack = self.gamestatus.rack
        self.over = self.gamestatus.over
        self.gamestatus.game_over()
        self.assertFalse(self.over)

    def test_game_over_true(self):
        self.gamestatus = GameStatus()
        # self.rack = self.gamestatus.rack
        self.over = self.gamestatus.over
        self.gamestatus.rack = [["yellow", "red", "yellow", "red", "yellow", "red", "yellow"], ["red", "yellow", "red", "yellow", "red", "yellow", "red"], ["red", "yellow", "red", "yellow", "red", "yellow", "red"], [
            "yellow", "red", "yellow", "red", "yellow", "red", "yellow"], ["yellow", "red", "yellow", "red", "yellow", "red", "yellow"], ["red", "yellow", "red", "yellow", "red", "yellow", "red"]]
        self.gamestatus.game_over()
        self.assertTrue(self.over)
