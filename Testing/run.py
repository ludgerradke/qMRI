import unittest as ut
from Testing.TestDataCreator import TestDicomCreator
from Testing.TestDatabase import TestDatabase


if __name__ == '__main__':
    TestDicomCreator()
    TestDatabase()
    ut.main()
