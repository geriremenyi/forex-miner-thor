import unittest
import datetime

from forex_miner_thor.model.candle import Candle, Candlestick


class TestCandle(unittest.TestCase):
    def test_init(self):
        # Arrange
        time = datetime.datetime.now()
        volume = 12345
        bid = Candlestick(1.2, 1.3, 1.0, 1.1)
        mid = Candlestick(1.3, 1.4, 1.1, 1.2)
        ask = Candlestick(1.4, 1.5, 1.2, 1.3)

        # Act
        candle = Candle(time, volume, bid, mid, ask)

        # Assert
        self.assertEqual(candle.time, time)
        self.assertEqual(candle.volume, volume)
        self.assertEqual(candle.bid, bid)
        self.assertEqual(candle.mid, mid)
        self.assertEqual(candle.ask, ask)


if __name__ == '__main__':
    unittest.main()

