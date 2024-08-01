import unittest
from refmanual import ReferenceManualGenerator

class TestReferenceManualGenerator(unittest.TestCase):
    def test_generate_reference_manual(self):
        expected_manual = [
            "1: White Blue", "2: White Orange",
            "3: White Green", "4: White Brown",
            "5: White Slate", "6: Red Blue",
            "7: Red Orange", "8: Red Green",
            "9: Red Brown",
            "10: Red Slate",
            "11: Black Blue",
            "12: Black Orange",
            "13: Black Green",
            "14: Black Brown",
            "15: Black Slate",
            "16: Yellow Blue",
            "17: Yellow Orange",
            "18: Yellow Green",
            "19: Yellow Brown",
            "20: Yellow Slate",
            "21: Violet Blue",
            "22: Violet Orange",
            "23: Violet Green",
            "24: Violet Brown",
            "25: Violet Slate"
        ]
        actual_manual = ReferenceManualGenerator.generate_reference_manual()
        self.assertEqual(actual_manual, expected_manual)
