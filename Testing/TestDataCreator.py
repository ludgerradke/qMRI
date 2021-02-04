import unittest as ut
import random
import string
import os
from glob import glob
import shutil

from Testing.utils import create_test_dicom, create_dicom_folder


class TestDicomCreator(ut.TestCase):
    print("start TestDicomCreator")

    def test_dicom_is_created(self):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '.dcm'
        create_test_dicom(filename)
        self.assertTrue(os.path.isfile(filename))
        os.remove(filename)

    def test_dicom_folder_is_created(self):
        number = 10
        folder = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        create_dicom_folder(folder, number)
        self.assertTrue(os.path.exists(folder))
        self.assertTrue(len(glob(folder + '/*')), number)
        shutil.rmtree(folder)

