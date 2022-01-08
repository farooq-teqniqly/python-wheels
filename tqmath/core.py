import numpy as np


def matrix_multiply(array1: list, array2: list):
    np_array1 = np.array(array1)
    np_array2 = np.array(array2)
    result = np.multiply(np_array1, np_array2)

    return [list(a) for a in list(result)]
