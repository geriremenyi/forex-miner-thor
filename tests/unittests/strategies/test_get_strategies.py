import unittest
import pandas as pd

from forex_miner_thor.strategies.get_strategies import get_strategies
from forex_miner_thor.strategies.ema.ema_strategy import EmaStrategy


class TestGetStrategies(unittest.TestCase):
    def test_get_strategies(self):
        # Arrange
        instrument = 'EUR_USD'
        data = pd.DataFrame(data={
            'Time': ['2010-01-03 17:00:00+00:00', '2010-01-03 18:00:00+00:00'],
            'Open': [1.4312, 1.43172],
            'High': [1.43172, 1.43425],
            'Low': [1.4312, 1.43105],
            'Close': [1.43172, 1.43157],
            'Volume': [3, 137]
        })

        # Act
        strategies = get_strategies(instrument, data)

        # Assert
        self.assertEqual(len(strategies), 1)
        self.assertEqual(type(strategies[0]), EmaStrategy)


if __name__ == '__main__':
    unittest.main()

