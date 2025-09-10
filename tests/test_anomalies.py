# tests/test_anomalies.py
import numpy as np

def spi(values):
    # toy SPI: z-score with tiny epsilon to avoid divide-by-zero
    arr = np.asarray(values, dtype=float)
    return (arr - arr.mean()) / (arr.std() + 1e-9)

def is_ndvi_anomaly(ndvi_vals, threshold=-0.2):
    # return a plain Python bool so tests don’t trip on np.bool_
    return bool(np.asarray(ndvi_vals)[-1] < threshold)

def test_spi_basic():
    vals = [1, 2, 3, 4, 5]
    z = spi(vals)
    assert abs(z.mean()) < 1e-6
    assert len(z) == 5

def test_ndvi_anomaly_flag():
    ndvi = [0.35, 0.31, 0.14, -0.25]  # last value is below -0.2
    assert is_ndvi_anomaly(ndvi)  # truthy check
