from colorpair import ColorPair
import unittest

class TestColorPair(unittest.TestCase):
    def test_number_to_pair(self):
        test_cases = [
            (1, 'White', 'Blue'),
            (2, 'White', 'Orange'),
            # Add more test cases as needed
        ]
        for pair_number, expected_major_color, expected_minor_color in test_cases:
            major_color, minor_color = ColorPair.get_color_from_pair_number(pair_number)
            self.assertEqual(major_color, expected_major_color)
            self.assertEqual(minor_color, expected_minor_color)

    def test_pair_to_number(self):
        test_cases = [
            ('White', 'Blue', 1),
            ('White', 'Orange', 2),
            # Add more test cases as needed
        ]
        for major_color, minor_color, expected_pair_number in test_cases:
            pair_number = ColorPair.get_pair_number_from_color(major_color, minor_color)
            self.assertEqual(pair_number, expected_pair_number)

    def test_generate_reference_manual(self):
        expected_manual = [
            "1: White Blue",
            "2: White Orange",
            "3: White Green",
            "4: White Brown",
            "5: White Slate",
            "6: Red Blue",
            "7: Red Orange",
            "8: Red Green",
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
        
        actual_manual = []
        for pair_number in range(1, 26):
            major_color, minor_color = ColorPair.get_color_from_pair_number(pair_number)
            actual_manual.append(f"{pair_number}: {ColorPair.color_pair_to_string(major_color, minor_color)}")
        self.assertEqual(actual_manual, expected_manual)


