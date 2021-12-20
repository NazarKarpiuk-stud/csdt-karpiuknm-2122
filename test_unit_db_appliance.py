import unittest
from db_appliance import createTable, insertResult


class TestBdAppliance(unittest.TestCase):
    def testTableArgs(self):
        self.assertRaises(TypeError, createTable, -1)

    def testQueryArgs(self):
        self.assertRaises(TypeError, createTable, (1, True, 10, False))
        self.assertRaises(TypeError, createTable, ({"one", "two", "three", "four"}))
