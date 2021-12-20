import unittest
from binaryTransformation import convertToBinaryData


class TestImageTransform(unittest.TestCase):
    def testBinaryTr(self):
        binaryString = convertToBinaryData("Resources/image5.jpg")
        self.assertIsInstance(binaryString, bytes)

    def testBinaryArgs(self):
        self.assertRaises(TypeError, convertToBinaryData, -1)
        self.assertRaises(TypeError, convertToBinaryData, 3j)
        self.assertRaises(TypeError, convertToBinaryData, b"Hello")
        self.assertRaises(TypeError, convertToBinaryData, True)
        self.assertRaises(TypeError, convertToBinaryData, range(6))
