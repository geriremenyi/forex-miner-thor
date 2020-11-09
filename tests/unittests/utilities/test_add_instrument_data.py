import unittest
import unittest.mock as mock
import pandas as pd
from datetime import datetime
from pathlib import Path
import shutil

from forex_miner_thor.model.candle import Candle, Candlestick
from forex_miner_thor.utilities.add_instrument_data import add_instrument_data


class TestAddInstrumentData(unittest.TestCase):
    def setUp(self) -> None:
        temp_dir = (Path(__file__).parent.resolve() / '..' / '..' / 'temp').resolve()
        if not temp_dir.is_dir():
            temp_dir.mkdir()

    def tearDown(self) -> None:
        temp_dir = (Path(__file__).parent.resolve() / '..' / '..' / 'temp').resolve()
        if temp_dir.is_dir():
            shutil.rmtree(temp_dir)

    @staticmethod
    def create_temp_file(file_name) -> Path:
        temp_dir = (Path(__file__).parent.resolve() / '..' / '..' / 'temp').resolve()
        temp_file = temp_dir / file_name
        if not temp_file.is_file():
            temp_file.write_text('')

        return temp_file.resolve()

    @mock.patch('forex_miner_thor.utilities.add_instrument_data.get_instrument_data')
    @mock.patch('forex_miner_thor.utilities.add_instrument_data.get_or_create_instrument_file')
    def test_add(self, get_or_create_instrument_file: mock.MagicMock, get_instrument_data: mock.MagicMock):
        # Arrange
        instrument_data = pd.DataFrame(data={
            'Open': [1.4312, 1.43172],
            'High': [1.43172, 1.43425],
            'Low': [1.4312, 1.43105],
            'Close': [1.43172, 1.43157],
            'Volume': [3, 137]
        }, index=[
            datetime.fromisoformat('2010-01-03 17:00:00+00:00'),
            datetime.fromisoformat('2010-01-03 18:00:00+00:00')
        ])
        get_instrument_data.return_value = instrument_data
        get_or_create_instrument_file.return_value = self.create_temp_file('test_add_file.csv')

        candles = Candle(
            datetime.fromisoformat('2010-01-03 19:00:00+00:00'),
            200,
            Candlestick(1.43152, 1.43155, 1.43145, 1.43145),
            Candlestick(1.43157, 1.43160, 1.43150, 1.43150),
            Candlestick(1.43162, 1.43165, 1.43155, 1.43155)
        )

        # Act
        data = add_instrument_data('EUR_USD', 'H1', [candles])

        # Assert
        self.assertEqual(get_instrument_data.call_count, 1)
        self.assertEqual(get_or_create_instrument_file.call_count, 1)
        self.assertEqual(len(data), 3)
        self.assertEqual(data.iloc[-1]['Volume'], 200)
        self.assertEqual(data.iloc[-1]['Open'], 1.43157)
        self.assertEqual(data.iloc[-1]['High'], 1.43160)
        self.assertEqual(data.iloc[-1]['Low'], 1.43150)
        self.assertEqual(data.iloc[-1]['Close'], 1.43150)

    @mock.patch('forex_miner_thor.utilities.add_instrument_data.get_instrument_data')
    @mock.patch('forex_miner_thor.utilities.add_instrument_data.get_or_create_instrument_file')
    def test_add_duplicate(self, get_or_create_instrument_file: mock.MagicMock, get_instrument_data: mock.MagicMock):
        # Arrange
        instrument_data = pd.DataFrame(data={
            'Open': [1.4312, 1.43172],
            'High': [1.43172, 1.43425],
            'Low': [1.4312, 1.43105],
            'Close': [1.43172, 1.43157],
            'Volume': [3, 137]
        }, index=[
            datetime.fromisoformat('2010-01-03 17:00:00+00:00'),
            datetime.fromisoformat('2010-01-03 18:00:00+00:00')
        ])
        get_instrument_data.return_value = instrument_data
        get_or_create_instrument_file.return_value = self.create_temp_file('test_add_file.csv')

        candles = Candle(
            datetime.fromisoformat('2010-01-03 18:00:00+00:00'),
            200,
            Candlestick(1.43152, 1.43155, 1.43145, 1.43145),
            Candlestick(1.43157, 1.43160, 1.43150, 1.43150),
            Candlestick(1.43162, 1.43165, 1.43155, 1.43155)
        )

        # Act
        data = add_instrument_data('EUR_USD', 'H1', [candles])

        # Assert
        self.assertEqual(get_instrument_data.call_count, 1)
        self.assertEqual(get_or_create_instrument_file.call_count, 1)
        self.assertEqual(len(data), 2)
        self.assertEqual(data.iloc[-1]['Volume'], 200)
        self.assertEqual(data.iloc[-1]['Open'], 1.43157)
        self.assertEqual(data.iloc[-1]['High'], 1.43160)
        self.assertEqual(data.iloc[-1]['Low'], 1.43150)
        self.assertEqual(data.iloc[-1]['Close'], 1.43150)


if __name__ == '__main__':
    unittest.main()

