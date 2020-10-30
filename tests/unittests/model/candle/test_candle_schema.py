import unittest

from marshmallow import fields

from forex_miner_thor.model.candle import CandleSchema


class TerstCandleSchema(unittest.TestCase):
    def test_init(self):
        # Arrange
        # Act
        candle_schema = CandleSchema()

        # Assert
        self.assertEqual(type(candle_schema.fields["time"]), fields.DateTime)
        self.assertEqual(type(candle_schema.fields["volume"]), fields.Integer)
        self.assertEqual(type(candle_schema.fields["bid"]), fields.Nested)
        self.assertEqual(type(candle_schema.fields["mid"]), fields.Nested)
        self.assertEqual(type(candle_schema.fields["ask"]), fields.Nested)


if __name__ == '__main__':
    unittest.main()

