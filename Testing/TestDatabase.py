import unittest as ut

import numpy as np

from Database.connect import connect


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