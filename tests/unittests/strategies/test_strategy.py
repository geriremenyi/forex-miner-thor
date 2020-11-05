import unittest

from forex_miner_thor.model.trade import TradeDirection, TradeSignal
from tests.unittests.strategies import MockStrategy


class TestStrategy(unittest.TestCase):
    def test_abstract_strategy(self):
        # Arrange
        # Act
        strategy = MockStrategy(TradeSignal('EUR_USD', TradeDirection.SHORT, 1.0))

        # Assert
        self.assertIsNotNone(getattr(strategy, 'apply', None))
        self.assertTrue(callable(getattr(strategy, 'apply', None)))


if __name__ == '__main__':
    unittest.main()