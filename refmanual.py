
from colorpair import ColorPair

class ReferenceManualGenerator:
    @staticmethod
    def generate_reference_manual():
        manual = []
        for pair_number in range(1, 26):
            major_color, minor_color = ColorPair.get_color_from_pair_number(pair_number)
            manual.append(f"{pair_number}: {ColorPair.color_pair_to_string(major_color, minor_color)}")
        return manual