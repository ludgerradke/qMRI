import numpy as np
import pydicom

dtypes = {
    'int8': np.int8,
    'int16': np.int16,
    'int32': np.int32,
    'float16': np.float16,
    'float32': np.float32,
    'float64': np.float64,
}

encode = {
    "'int'": int,
    "'tuple'": tuple,
    "'float'": float,
    "'str'": str
}


def dicom_information_decode(arr):
    return str(type(arr)).replace('<class ','') .replace('>', '')


def dicom_information_encode(cls, string_arr):
    try:
        encoder = encode[cls]
    except KeyError:
        return string_arr
    return encoder(string_arr)
