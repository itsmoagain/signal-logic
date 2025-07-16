"""
signal_tools.py

Modular functions for climate signal detection:
- Standardized Precipitation Index (SPI)
- NDVI anomaly calculation

Intended for use in reproducibility-aware scientific software pipelines.
"""

import pandas as pd

def calculate_spi(precip_series: pd.Series, window: int = 6) -> pd.Series:
    """
    Approximates SPI using a rolling z-score.

    Args:
        precip_series (pd.Series): Time-indexed rainfall or precipitation values.
        window (int): Rolling window size in months (default is 6).

    Returns:
        pd.Series: Clipped SPI values between -3 and +3.
    """
    rolling_mean = precip_series.rolling(window=window, min_periods=3).mean()
    rolling_std = precip_series.rolling(window=window, min_periods=3).std()
    spi = (precip_series - rolling_mean) / rolling_std
    return spi.clip(lower=-3, upper=3)

def calculate_ndvi_anomaly(ndvi_series: pd.Series) -> pd.Series:
    """
    Computes NDVI anomaly as deviation from long-term mean.

    Args:
        ndvi_series (pd.Series): NDVI values over time.

    Returns:
        pd.Series: Anomaly values (positive = greener than average).
    """
    long_term_mean = ndvi_series.mean()
    return ndvi_series - long_term_mean
