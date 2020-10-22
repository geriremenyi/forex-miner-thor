from pathlib import Path


def get_or_create_instrument_file(instrument: str, granularity: str) -> Path:
    # Data directory
    data_directory = (Path.cwd() / '..' / 'data').resolve()
    if not data_directory.is_dir():
        data_directory.mkdir()

    # Instrument specific directory
    instrument_directory = data_directory / instrument
    if not instrument_directory.is_dir():
        instrument_directory.mkdir()

    # File path
    instrument_file = instrument_directory / (granularity + '.csv')
    if not instrument_file.is_file():
        instrument_file.write_text('Time,Open,High,Low,Close,Volume')

    return instrument_file.resolve()
