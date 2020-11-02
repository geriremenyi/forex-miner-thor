import unittest

from marshmallow import fields

from forex_miner_thor.model.trade import TradeSignalSchema


class TestTradeSignalSchema(unittest.TestCase):
    def test_init(self):
        # Arrange
        # Act
        trade_signal_schema = TradeSignalSchema()

        # Assert
        self.assertEqual(type(trade_signal_schema.fields["instrument"]), fields.String)
        self.assertEqual(type(trade_signal_schema.fields["direction"]), fields.String)
        self.assertEqual(type(trade_signal_schema.fields["confidence"]), fields.Float)

    def test_make(self):
        # Arrange
        instrument = 'EUR_USD'
        direction = 'long'
        confidence = 1.0

        # Act
        trade_signal_schema = TradeSignalSchema()
        trade_signal_make = trade_signal_schema.make_trade_signal(
            {
                'instrument': instrument,
                'direction': direction,
                'confidence': confidence,
            }
        )

        # Assert
        self.assertEqual(trade_signal_make.instrument, instrument)
        self.assertEqual(trade_signal_make.direction, direction)
        self.assertEqual(trade_signal_make.confidence, confidence)


if __name__ == '__main__':
    unittest.main()

