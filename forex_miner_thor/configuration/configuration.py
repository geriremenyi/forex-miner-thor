import os
import configparser as cf
import forex_miner_thor.configuration as conf


class Configuration(object):
    """
    A class used to represent a typed configuration.
    """
    def __init__(self):
        """
        Configuration constructor.

        Initializes the configuration using the
        correct .ini file based on the environment
        """
        self._raw_config = cf.ConfigParser()
        config_file_folder = os.path.join(os.path.dirname(__file__), '../../configurations')
        config_file_name = os.path.join(config_file_folder, 'configuration.dev.ini') \
            if os.environ.get('ENVIRONMENT') == "Development" \
            else os.path.join(config_file_folder, 'configuration.ini')
        self._raw_config.read(config_file_name, encoding='utf-8')
        self._instruments = conf.InstrumentsConfiguration(
            int(self._raw_config['instruments']['start_year']),
            self._raw_config['instruments']['api_url']
        )

    @property
    def instruments(self) -> conf.InstrumentsConfiguration:
        return self._instruments
