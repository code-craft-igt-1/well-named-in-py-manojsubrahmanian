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



