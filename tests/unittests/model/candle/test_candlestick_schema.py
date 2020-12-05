import unittest

from marshmallow import fields

from forex_miner_thor.model.candle import CandlestickSchema


class TestCandlestickSchema(unittest.TestCase):
    def test_init(self):
        # Arrange
        # Act
        candlestick_schema = CandlestickSchema()

        # Assert
        self.assertEqual(type(candlestick_schema.fields["open"]), fields.Float)
        self.assertEqual(type(candlestick_schema.fields["high"]), fields.Float)
        self.assertEqual(type(candlestick_schema.fields["low"]), fields.Float)
        self.assertEqual(type(candlestick_schema.fields["close"]), fields.Float)

    def test_make(self):
        # Arrange
        open = 1.2
        high = 1.4
        low = 1.1
        close = 1.3

        # Act
        candlestick_schema = CandlestickSchema()
        candlestick_make = candlestick_schema.make_candlestick({'open': open, 'high': high, 'low': low, 'close': close})

        # Assert
        self.assertEqual(candlestick_make.open, open)
        self.assertEqual(candlestick_make.high, high)
        self.assertEqual(candlestick_make.low, low)
        self.assertEqual(candlestick_make.close, close)


if __name__ == '__main__':
    unittest.main()

