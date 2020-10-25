from enum import Enum


class TradeDirection(Enum):
    LONG = "long"
    SHORT = "short"

    def __str__(self):
        return self.value

