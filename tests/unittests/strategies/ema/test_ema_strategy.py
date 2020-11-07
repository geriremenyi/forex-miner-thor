import unittest
import pandas as pd
from pathlib import Path

from forex_miner_thor.model.trade import TradeDirection
from forex_miner_thor.strategies.ema import EmaStrategy


class TestEmaStrategy(unittest.TestCase):
    @staticmethod
    def create_test_data(file_name) -> pd.DataFrame:
        file = (Path(__file__).parent.resolve() / '..' / '..' / '..' / 'data' / file_name).resolve()
        return pd.read_csv(file, parse_dates=['Time'], index_col='Time')

    def test_long(self):
        # Arrange
        instrument = 'EUR_USD'
        data = self.create_test_data('long_test.csv')
        ema_strategy = EmaStrategy(instrument, data)

        # Act
        trade_signal = ema_strategy.apply()

        # Assert
        self.assertIsNotNone(trade_signal)
        self.assertEqual(trade_signal.instrument, instrument)
        self.assertEqual(trade_signal.direction, TradeDirection.LONG)
        self.assertEqual(trade_signal.confidence, 1.0)

    def test_short(self):
        # Arrange
        instrument = 'EUR_USD'
        data = self.create_test_data('short_test.csv')
        ema_strategy = EmaStrategy(instrument, data)

        # Act
        trade_signal = ema_strategy.apply()

        # Assert
        self.assertIsNotNone(trade_signal)
        self.assertEqual(trade_signal.instrument, instrument)
        self.assertEqual(trade_signal.direction, TradeDirection.SHORT)
        self.assertEqual(trade_signal.confidence, 1.0)

    def test_none(self):
        # Arrange
        instrument = 'EUR_USD'
        data = self.create_test_data('none_test.csv')
        ema_strategy = EmaStrategy(instrument, data)

        # Act
        trade_signal = ema_strategy.apply()

        # Assert
        self.assertIsNone(trade_signal)


if __name__ == '__main__':
    unittest.main()

