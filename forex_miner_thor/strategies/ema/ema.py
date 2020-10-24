import pandas as pd


def ema(data: pd.Series, n: int) -> pd.Series:
    """
    Returns `n`-period exponential moving average of data
    """
    return pd.Series(data).ewm(n, adjust=False).mean()

