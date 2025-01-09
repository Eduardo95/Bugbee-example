from src import player
import unittest


class TestUtil(unittest.TestCase):
    def test_team_conversion(self):
        self.assertEqual(player.team_conversion(), "Stephen, Kobe, Ming")


if __name__ == '__main__':
    unittest.main()
