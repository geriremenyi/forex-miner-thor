import forex_miner_thor.client as client


class InstrumentsClient(client.Client):

    def __init__(self, base_url: str):
        super().__init__(base_url)

    def get_available_instruments(self):
        return self.get("")
