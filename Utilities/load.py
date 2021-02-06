import os
from glob import glob
import pydicom


def d_load(file: str):
    folder = os.path.dirname(file)
    d_files = glob(folder + '/*.dcm')
    d_list = [pydicom.dcmread(f) for f in d_files]
    return d_list