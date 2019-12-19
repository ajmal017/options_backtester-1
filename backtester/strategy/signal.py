from enum import Enum
from backtester.option import Direction

Signal = Enum("Signal", "ENTRY EXIT")

# Orders:
# BTO: Buy to Open
# BTC: Buy to Close
# STO: Sell to Open
# STC: Sell to Close
# Order = Enum("Order", "BTO BTC STO STC")


class Order(Enum):
    BTO = 'BTO'
    BTC = 'BTC'
    STO = 'STO'
    STC = 'STC'

    def __invert__(self):
        if self == Order.BTO:
            return Order.STC
        elif self == Order.BTC:
            return Order.STO
        elif self == Order.STO:
            return Order.BTC
        elif self == Order.STC:
            return Order.BTO


def get_order(direction, signal):
    """Returns Order type given direction (BUY | SELL) and
    signal (ENTRY | EXIT).
    """
    if direction == Direction.BUY:
        return Order.BTO if signal == Signal.ENTRY else Order.STC
    else:
        return Order.STO if signal == Signal.ENTRY else Order.BTC
