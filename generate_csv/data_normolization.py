import numpy as np

def minmax_normalization(data):
    xs_max = np.max(data, axis=0)
    xs_min = np.min(data, axis=0)
    xs = (1 - 0) * (data - xs_min) / (xs_max - xs_min) + 0
    return xs.round(4)
