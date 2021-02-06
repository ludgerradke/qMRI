import unittest as ut
from Testing.TestDataCreator import TestDicomCreator
from Testing.TestDatabase import TestDatabase
from Testing.TestUtilities import TestUtilities

if __name__ == '__main__':
    TestDicomCreator()
    TestDatabase()
    TestUtilities()
    ut.main()
