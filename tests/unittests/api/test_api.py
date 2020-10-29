import unittest
import unittest.mock as mock
import json
from typing import List

from forex_miner_thor.api import create_api
from forex_miner_thor.model.trade import TradeSignal, TradeDirection, TradeSignalSchema


class TestApi(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.api = create_api().test_client()
        # propagate the exceptions to the test client
        self.api.testing = True

    def test_report_status(self):
        # Arrange
        # Act
        response = self.api.get('/api/v1/engine')

        # Assert
        self.assertEqual(response.status_code, 200)

    @mock.patch('forex_miner_thor.api.api.add_instrument_data')
    @mock.patch('forex_miner_thor.api.api.apply_strategies')
    def test_tick_not_json(self, apply_strategies: mock.MagicMock, add_instrument_data: mock.MagicMock):
        # Arrange
        # Act
        response = self.api.post('/api/v1/engine/tick')

        # Assert
        self.assertEqual(add_instrument_data.call_count, 0)
        self.assertEqual(apply_strategies.call_count, 0)
        self.assertEqual(response.status_code, 415)

    @mock.patch('forex_miner_thor.api.api.add_instrument_data')
    @mock.patch('forex_miner_thor.api.api.apply_strategies')
    def test_tick_wrong(self, apply_strategies: mock.MagicMock, add_instrument_data: mock.MagicMock):
        # Arrange
        data = json.dumps([
            {
                'InvalidJson': 'Data'
            }
        ])
        content_type = "application/json"

        # Act
        response = self.api.post('/api/v1/engine/tick', data=data, content_type=content_type)

        # Assert
        self.assertEqual(add_instrument_data.call_count, 0)
        self.assertEqual(apply_strategies.call_count, 0)
        self.assertEqual(response.status_code, 422)

    @mock.patch('forex_miner_thor.api.api.add_instrument_data')
    @mock.patch('forex_miner_thor.api.api.apply_strategies')
    def test_tick_empty(self, apply_strategies: mock.MagicMock, add_instrument_data: mock.MagicMock):
        # Arrange
        content_type = "application/json"

        # Act
        response = self.api.post('/api/v1/engine/tick', content_type=content_type)

        # Assert
        self.assertEqual(add_instrument_data.call_count, 0)
        self.assertEqual(apply_strategies.call_count, 0)
        self.assertEqual(response.status_code, 500)

    @mock.patch('forex_miner_thor.api.api.add_instrument_data')
    @mock.patch('forex_miner_thor.api.api.apply_strategies')
    def test_tick_empty_array(self, apply_strategies: mock.MagicMock, add_instrument_data: mock.MagicMock):
        # Arrange
        data = json.dumps([])
        content_type = "application/json"

        # Act
        response = self.api.post('/api/v1/engine/tick', data=data, content_type=content_type)

        # Assert
        self.assertEqual(add_instrument_data.call_count, 0)
        self.assertEqual(apply_strategies.call_count, 0)
        self.assertEqual(response.status_code, 200)

    @mock.patch('forex_miner_thor.api.api.add_instrument_data')
    @mock.patch('forex_miner_thor.api.api.apply_strategies')
    def test_tick_trade_signal(self, apply_strategies: mock.MagicMock, add_instrument_data: mock.MagicMock):
        # Arrange
        candles = [
            {
                "time": "2000-01-01T00:00:00Z",
                "volume": 12345,
                "bid": {
                    "open": 1.1625,
                    "high": 1.1650,
                    "low": 1.1605,
                    "close": 1.1615
                },
                "mid": {
                    "open": 1.1625,
                    "high": 1.1650,
                    "low": 1.1605,
                    "close": 1.33
                },
                "ask": {
                    "open": 1.1625,
                    "high": 1.1650,
                    "low": 1.1605,
                    "close": 1.1615
                }
            }
        ]
        data = json.dumps([
            {
                "instrument": "EUR_USD",
                "granularity": "H1",
                'candles': candles
            }
        ])
        content_type = "application/json"
        add_instrument_data.return_value = {
            'Time': candles[0]['time'],
            'Volume': candles[0]['volume'],
            'Open': candles[0]['mid']['open'],
            'High': candles[0]['mid']['high'],
            'Low': candles[0]['mid']['low'],
            'Close': candles[0]['mid']['close']
        }
        trade_signal = TradeSignal("EUR_USD", TradeDirection.LONG, 1.0)
        trade_signals: List[TradeSignal] = [trade_signal]
        trade_signals_json = TradeSignalSchema(many=True).dump(trade_signals)
        apply_strategies.return_value = trade_signal

        # Act
        response = self.api.post('/api/v1/engine/tick', data=data, content_type=content_type)

        # Assert
        self.assertEqual(add_instrument_data.call_count, 1)
        self.assertEqual(apply_strategies.call_count, 1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), trade_signals_json)

    @mock.patch('forex_miner_thor.api.api.add_instrument_data')
    def test_add_instrument_granularity_candles_wrong(self, add_instrument_data: mock.MagicMock):
        # Arrange
        data = json.dumps([
            {
                'InvalidJson': 'Data'
            }
        ])
        content_type = "application/json"

        # Act
        response = self.api.post('/api/v1/engine/instruments/EUR_USD/granularities/H1', data=data, content_type=content_type)

        # Assert
        self.assertEqual(add_instrument_data.call_count, 0)
        self.assertEqual(response.status_code, 422)

    @mock.patch('forex_miner_thor.api.api.add_instrument_data')
    def test_add_instrument_granularity_candles_empty(self, add_instrument_data: mock.MagicMock):
        # Arrange
        content_type = "application/json"

        # Act
        response = self.api.post('/api/v1/engine/instruments/EUR_USD/granularities/H1', content_type=content_type)

        # Assert
        self.assertEqual(add_instrument_data.call_count, 0)
        self.assertEqual(response.status_code, 500)

    @mock.patch('forex_miner_thor.api.api.add_instrument_data')
    def test_add_instrument_granularity_candles_array(self, add_instrument_data: mock.MagicMock):
        # Arrange
        data = json.dumps([])
        content_type = "application/json"

        # Act
        response = self.api.post('/api/v1/engine/instruments/EUR_USD/granularities/H1', data=data, content_type=content_type)

        # Assert
        self.assertEqual(add_instrument_data.call_count, 1)
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
