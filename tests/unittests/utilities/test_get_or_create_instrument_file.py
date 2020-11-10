import unittest
from pathlib import Path
import shutil

from forex_miner_thor.utilities.get_or_create_instrument_file import get_or_create_instrument_file


class TestGetOrCreateInstrumentFile(unittest.TestCase):
    def tearDown(self) -> None:
        data_directory = (Path(__file__).parent.resolve() / '..' / '..' / '..' / 'data').resolve()
        if data_directory.is_dir():
            test_instrument_folder = (data_directory / 'TEST').resolve()
            shutil.rmtree(test_instrument_folder)

    def test_get_or_create(self):
        # Arrange
        instrument = 'TEST'
        granularity = 'TEST'

        # Act
        file = get_or_create_instrument_file(instrument, granularity)

        # Assert
        self.assertEqual(file.name, 'TEST.csv')


if __name__ == '__main__':
    unittest.main()

