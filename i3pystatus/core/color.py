from colour import Color


class ColorRangeModule(object):
    """
    Class to dynamically generate and select colors.

    Requires the PyPI package `colour`
    """

    start_color = "#00FF00"
    end_color = 'red'

    @staticmethod
    def get_hex_color_range(start_color, end_color, quantity):
        """
        Generates a list of quantity Hex colors from start_color to end_color.

        :param start_color: Hex or plain English color for start of range
        :param end_color: Hex or plain English color for end of range
        :param quantity: Number of colours to return
        :return: A list of Hex color values
        """
        pass

    def get_gradient(self, value, colors, upper_limit=100):
        """
        Map a value to a color
        :param value: Some value
        :return: A Hex color code
        """
        pass

    @staticmethod
    def percentage(part, whole):
        """
        Calculate percentage
        """
        pass
