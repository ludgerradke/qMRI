from Testing.DICOM import create_test_dicom
import unittest as ut
import random
import string
import os


class Test(ut.TestCase):

    def test_dicom_is_created(self):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '.dcm'
        create_test_dicom(filename)
        self.assertTrue(os.path.isfile(filename))
        os.remove(filename)


if __name__ == '__main__':
    ut.main()
