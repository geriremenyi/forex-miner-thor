import unittest

from forex_miner_thor.model.candle import Candlestick


class TestCandlestick(unittest.TestCase):
    def test_init(self):
        # Arrange
        open = 1.2
        high = 1.4
        low = 1.1
        close = 1.3

        # Act
        candlestick = Candlestick(open, high, low, close)

        # Assert
        self.assertEqual(candlestick.open, open)
        self.assertEqual(candlestick.high, high)
        self.assertEqual(candlestick.low, low)
        self.assertEqual(candlestick.close, close)


if __name__ == '__main__':
    unittest.main()

