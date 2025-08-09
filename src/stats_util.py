import numpy as np

def rec_moy(lists):
    arr = np.array(lists)
    return np.mean(arr)

def rec_variance(lists):
    arr = np.array(lists)
    return np.var(arr)

def rec_ecart_type(lists):
    arr = np.array(lists)
    return np.std(arr)
