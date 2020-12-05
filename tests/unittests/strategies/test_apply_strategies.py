import unittest
import unittest.mock as mock
import pandas as pd

from forex_miner_thor.strategies.apply_strategies import apply_strategies
from forex_miner_thor.model.trade import TradeDirection, TradeSignal

from tests.unittests.strategies import MockStrategy


class TestApplyStrategy(unittest.TestCase):
    @mock.patch('forex_miner_thor.strategies.apply_strategies.get_strategies')
    def test_no_strategy(self, get_strategies: mock.MagicMock):
        # Arrange
        instrument = 'EUR_USD'
        get_strategies.return_value = []

        # Act
        selected_strategy = apply_strategies(instrument, pd.DataFrame())

        # Assert
        self.assertEqual(get_strategies.call_count, 1)
        self.assertIsNone(selected_strategy)

    @mock.patch('forex_miner_thor.strategies.apply_strategies.get_strategies')
    def test_one_strategy(self, get_strategies: mock.MagicMock):
        # Arrange
        instrument = 'EUR_USD'
        mock_strategy = MockStrategy(TradeSignal(instrument, TradeDirection.LONG, 1.0))
        get_strategies.return_value = [mock_strategy]

        # Act
        selected_strategy = apply_strategies(instrument, pd.DataFrame())

        # Assert
        self.assertEqual(get_strategies.call_count, 1)
        self.assertEqual(selected_strategy, mock_strategy.trade_signal)

    @mock.patch('forex_miner_thor.strategies.apply_strategies.get_strategies')
    def test_multiple_strategies(self, get_strategies: mock.MagicMock):
        # Arrange
        instrument = 'EUR_USD'
        mock_strategy1 = MockStrategy(TradeSignal(instrument, TradeDirection.SHORT, 0.1))
        mock_strategy2 = MockStrategy(TradeSignal(instrument, TradeDirection.LONG, 0.2))
        mock_strategy_selected = MockStrategy(TradeSignal(instrument, TradeDirection.LONG, 0.6))
        mock_strategy3 = MockStrategy(TradeSignal(instrument, TradeDirection.SHORT, 0.3))
        mock_strategy4 = MockStrategy(TradeSignal(instrument, TradeDirection.LONG, 0.4))
        get_strategies.return_value = [
            mock_strategy1,
            mock_strategy2,
            mock_strategy_selected,
            mock_strategy3,
            mock_strategy4
        ]

        # Act
        selected_strategy = apply_strategies(instrument, pd.DataFrame())

        # Assert
        self.assertEqual(get_strategies.call_count, 1)
        self.assertEqual(selected_strategy, mock_strategy_selected.trade_signal)


if __name__ == '__main__':
    unittest.main()

