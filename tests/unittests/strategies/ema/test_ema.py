import unittest
import pandas as pd

from forex_miner_thor.strategies.ema.ema import ema


class TestEma(unittest.TestCase):
    def test_ema(self):
        # Arrange
        n = 3
        data = pd.Series([1, 2, 3, 4, 5])

        # Act
        ema_results = ema(data, n)

        # Assert
        self.assertEqual(ema_results[0], 1.0)
        self.assertEqual(ema_results[1], 1.25)
        self.assertEqual(ema_results[2], 1.6875)
        self.assertEqual(ema_results[3], 2.265625)
        self.assertEqual(ema_results[4], 2.94921875)


if __name__ == '__main__':
    unittest.main()

