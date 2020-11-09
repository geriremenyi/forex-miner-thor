import unittest
import unittest.mock as mock
from pathlib import Path

from forex_miner_thor.utilities.get_instrument_data import get_instrument_data


class TestAddInstrumentData(unittest.TestCase):
    @mock.patch('forex_miner_thor.utilities.get_instrument_data.get_or_create_instrument_file')
    def test_get_instrument_data(self, get_or_create_instrument_file: mock.MagicMock):
        # Arrange
        get_or_create_instrument_file.return_value = (
                Path(__file__).parent.resolve() / '..' / '..' / 'data' / 'none_test.csv'
        ).resolve()

        # Act
        data = get_instrument_data('EUR_USD', 'M1')

        # Assert
        self.assertEqual(get_or_create_instrument_file.call_count, 1)
        self.assertEqual(len(data), 200)


if __name__ == '__main__':
    unittest.main()

