import unittest
from unittest.mock import patch
from gameloop import GameLoop
from gamestatus import GameStatus
from minimax import Minimax


class TestGameLoop(unittest.TestCase):
    """Tests class gameloop."""

    def setUp(self):
        self.game = GameLoop()

    def test_init(self):
        self.game = GameLoop()
        self.game.gamestatus = GameStatus(self.game.gamerack)
        self.game.minimax = Minimax(self.game.gamerack, self.game.gamestatus)
        self.game.who_starts = None
        self.game.gamerack.players_color = None
        self.game.gamerack.ai_color = None
        self.game.turn = None
        self.assertEqual(self.game.who_starts, None)
        self.assertEqual(self.game.gamerack.players_color, None)
        self.assertEqual(self.game.gamerack.ai_color, None)
        self.assertEqual(self.game.turn, None)

    @patch("builtins.input", lambda _: "yes")
    def test_main_yes(self):
        """Tests if variable self.turn is true, when self.who_starts is yes."""
        self.game = GameLoop()
        self.game.who_starts = input(
            "Do you want the first move? Type 'yes' or 'no'. ")
        self.assertEqual(self.game.who_starts, "yes")
        #self.assertTrue(self.game.turn)

    @patch("builtins.input", lambda _: "no")
    def test_main_no(self):
        """Tests if variable self.turn is true, when self.who_starts is yes."""
        self.game = GameLoop()
        self.game.who_starts = input(
            "Do you want the first move? Type 'yes' or 'no'. ")
        self.assertEqual(self.game.who_starts, "no")
        #self.assertFalse(self.game.turn)

    def main_who_value_error(self):
        """Tests if function raises value error for wrong input word."""
        pass

    @patch("builtins.input", lambda _: "R")
    def test_main_red(self):
        """Tests if variable self.ai_color is yellow, when self.players_color is red."""
        self.game = GameLoop()
        self.game.gamerack.players_color = input("Choose your pawn's color: 'R' for red or 'Y' for yellow. ")
        self.assertEqual(self.game.gamerack.players_color, "R")
        #self.assertEqual(self.game.ai_color, "Y")

    @patch("builtins.input", lambda _: "Y")
    def test_main_yellow(self):
        """Tests if variable self.ai_color is red, when self.players_color is yellow."""
        self.game = GameLoop()
        self.game.gamerack.players_color = input("Choose your pawn's color: 'R' for red or 'Y' for yellow. ")
        self.assertEqual(self.game.gamerack.players_color, "Y")
        #self.assertEqual(self.game.ai_color, "R")

    def main_color_value_error(self):
        """Tests if function raises value error for wrong input color."""
        self.game = GameLoop()
        self.game.players_color = "5"
        self.assertRaises(ValueError, self.game.gamerack.players_color)

    def while_loop(self):
        """Tests while loop."""
        self.game = GameLoop()
        self.game.gamestatus.is_game_over = False
        self.game.turn = True
