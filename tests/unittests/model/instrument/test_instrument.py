import unittest

from forex_miner_thor.model.instrument import Instrument


class TestInstrument(unittest.TestCase):
    def test_init(self):
        # Arrange
        instrument_name = 'EUR_USD'
        granularity = 'H1'
        candles = []

        # Act
        instrument = Instrument(instrument_name, granularity, candles)

        # Assert
        self.assertEqual(instrument.instrument, instrument_name)
        self.assertEqual(instrument.granularity, granularity)
        self.assertEqual(instrument.candles, candles)


if __name__ == '__main__':
    unittest.main()

