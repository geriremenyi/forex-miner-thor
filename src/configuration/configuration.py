import configparser


class Configuration(object):
    def __init__(self, config_file):
        self._configs = configparser.ConfigParser()
        self._configs.read_file(config_file)

    @property
    def instrument_start_year(self):
        return self.