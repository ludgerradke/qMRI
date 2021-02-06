import unittest as ut

import numpy as np

from Database.connect import connect
from Utilities import *
from Testing.TestDataCreator import *


class TestDatabase(ut.TestCase):
    print("start TestDatabase")

    def test_create_db(self):
        con = connect('data')

    def test_add_get_2D_array(self):
        a = np.array([[1, 1], [1, 2]])
        con = connect('data')
        con.add("d_array", a)
        b = con.get("d_array", 0)
        self.assertEqual(a.any(), b.any())

    def test_add_get_3D_array(self):
        a = np.ones((3, 3, 3))
        con = connect('data')
        con.add("d_array", a)
        b = con.get("d_array", 0)
        self.assertEqual(a[0].any(), b.any())

    def test_add_get_int_information(self):
        con = connect('data')
        number1 = 12
        con.add("d_information", ('numberOfImages', number1))
        number2 = con.get("d_information", 'numberOfImages')
        self.assertEqual(number1, number2)

    def test_add_get_str_information(self):
        con = connect('data')
        text = "hallo"
        con.add("d_information", ('max_size', text))
        number2 = con.get("d_information", 'max_size')
        self.assertEqual(text, number2)

    def test_connect_in_two_function(self):
        def func1(key, text):
            con = connect('data')
            con.add("d_information", (key, text))

        def func2(key):
            con = connect('data')
            return con.get("d_information", key)

        key = 'key'
        text = 'Hallo'
        func1(key, text)
        self.assertEqual(text, func2(key))

    def test_add_get_dicom_array_and_information(self):
        create_dicom_test_folder('test', 10)
        files = glob(r'test\*.dcm')
        d_list = d_load(files[0])
        delete_dicom_test_folder('test')
        array, info = transform_dicom_ds_list_to_array(d_list, True)
        con = connect('data')

        with self.subTest():
            con.add('d_array', array)
            b = con.get('d_array', 0)
            self.assertEqual(array[0].any(), b.any())

        with self.subTest():
            keys = list(info.keys())
            for choice in range(len(keys)):
                con.add('d_information', (keys[choice], info.get(keys[choice])))
                b = con.get('d_information', keys[choice])
                if type(info[keys[choice]]) in [int, float, tuple, str]:
                    self.assertEqual(info[keys[choice]], b)
                else:
                    self.assertEqual(str(info[keys[choice]]), b)

        with self.subTest():
            for choice in range(len(keys)):
                if type(info[keys[choice]]) == int:
                    info[keys[choice]] = 1
                elif type(info[keys[choice]]) == float:
                    info[keys[choice]] = 1.0
                elif type(info[keys[choice]]) == str:
                    info[keys[choice]] = 'Test'
                else:
                    continue
                con.add('d_information', (keys[choice], info.get(keys[choice])))
                b = con.get("d_information", keys[choice])
                self.assertEqual(info[keys[choice]], b)
