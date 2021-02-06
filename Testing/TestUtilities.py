import unittest as ut
from glob import glob

import numpy as np

from Testing.utils import create_dicom_test_folder, delete_dicom_test_folder
from Utilities import *


class TestUtilities(ut.TestCase):
    print("start TestDicomCreator")

    def test_dicom_load_and_connect_to_database(self):
        with self.subTest():
            create_dicom_test_folder('test', 10)
            files = glob(r'test\*.dcm')
            d_list = d_load(files[0])
            delete_dicom_test_folder('test')
            self.assertTrue(len(d_list) == 10)

        with self.subTest():
            ds = d_list[0]
            array = ds.pixel_array
            self.assertTrue(type(array) == np.ndarray)

        with self.subTest():
            array, info = transform_dicom_ds_list_to_array(d_list)
            self.assertTrue(len(array.shape) == 3)

        with self.subTest():
            _, info = transform_dicom_ds_list_to_array(d_list, False)
            self.assertTrue(info is None)

        with self.subTest():
            _, info = transform_dicom_ds_list_to_array(d_list, True)
            self.assertTrue(type(info) is dict)

