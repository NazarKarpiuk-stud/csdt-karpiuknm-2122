import unittest
from db_appliance import insertResult


class IntegrTestTransormAndInsert(unittest.TestCase):
    def testExtentionAndType(self):
        self.assertRaises(
            TypeError,
            insertResult,
            ("December18", "18/12/2021 14:02:13", "Resources/video.mp4", "AB1234CD"),
        )
        self.assertRaises(
            TypeError,
            insertResult,
            ("December18", "18/12/2021 14:02:13", 0, "AB1234CD"),
        )
        self.assertRaises(
            TypeError, insertResult, ("December18", "18/12/2021 14:02:13", "AB1234CD")
        )
