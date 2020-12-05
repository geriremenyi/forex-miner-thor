import unittest

from forex_miner_thor.model.trade import TradeDirection, TradeSignal


class TestTradeSignal(unittest.TestCase):
    def test_init(self):
        # Arrange
        instrument = 'EUR_USD'
        direction = TradeDirection.LONG
        confidence = 1.0

        # Act
        trade_signal = TradeSignal(instrument, direction, confidence)

        # Assert
        self.assertEqual(trade_signal.instrument, instrument)
        self.assertEqual(trade_signal.direction, direction)
        self.assertEqual(trade_signal.confidence, confidence)


if __name__ == '__main__':
    unittest.main()

