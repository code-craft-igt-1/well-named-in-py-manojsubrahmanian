class ColorPair:
    MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]
    MAJOR_COLORS = ["White", "Red", "Black", "Yellow", "Violet"]

    @staticmethod
    def color_pair_to_string(major_color, minor_color):
        return f'{major_color} {minor_color}'

    @staticmethod
    def get_color_from_pair_number(pair_number):
        zero_based_pair_number = pair_number - 1
        major_index = zero_based_pair_number // len(ColorPair.MINOR_COLORS)
        if major_index >= len(ColorPair.MAJOR_COLORS):
            raise Exception('Major index out of range')
        minor_index = zero_based_pair_number % len(ColorPair.MINOR_COLORS)
        if minor_index >= len(ColorPair.MINOR_COLORS):
            raise Exception('Minor index out of range')
        return ColorPair.MAJOR_COLORS[major_index], ColorPair.MINOR_COLORS[minor_index]

    @staticmethod
    def get_pair_number_from_color(major_color, minor_color):
        try:
            major_index = ColorPair.MAJOR_COLORS.index(major_color)
        except ValueError:
            raise Exception('Major index out of range')
        try:
            minor_index = ColorPair.MINOR_COLORS.index(minor_color)
        except ValueError:
            raise Exception('Minor index out of range')
        return major_index * len(ColorPair.MINOR_COLORS) + minor_index + 1