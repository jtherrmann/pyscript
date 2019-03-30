from . import Shape
import math


# TODO: tests


class Polygon(Shape):

    def __init__(self, num_sides, side_length):
        self._num_sides = num_sides
        self._side_length = side_length
        self._calculate_height_width()

    def _set_width(self, width):
        self._width = width

    def _set_height(self, height):
        self._height = height

    def _get_width(self):
        return self._width

    def _get_height(self):
        return self._height

    # TODO: refactor
    def _calculate_height_width(self):
        if self._num_sides % 2 != 0:
            self._set_height(
                self._side_length
                * (1 + math.cos(math.pi / self._num_sides))
                / (2 * math.sin(math.pi / self._num_sides))
            )
            self._set_width(
                (self._side_length
                 * math.sin(math.pi
                            * (self._num_sides - 1) / (2 * self._num_sides)))
                / (math.sin(math.pi / self._num_sides))
            )
        elif self._num_sides % 4 == 0:
            self._set_height(
                self._side_length
                * (math.cos(math.pi / self._num_sides))
                / (math.sin(math.pi / self._num_sides))
            )
            self._set_width(
                (self._side_length * math.sin(math.pi / self._num_sides))
                / (math.sin(math.pi / self._num_sides))
            )
        else:
            self._set_height(
                self._side_length
                * (math.cos(math.pi / self._num_sides))
                / (math.sin(math.pi / self._num_sides))
            )
            self._set_width(self._side_length
                            / (math.sin(math.pi / self._num_sides)))

    def _get_postscript(self, center):
        total_angle = (self._num_sides - 2) * 180
        interior_angle = str(180 - (total_angle / self._num_sides))

        translate_x = self._side_length / -2
        translate_y = self._get_height() / -2

        return self._join_lines(
            "gsave",
            f"{translate_x} {translate_y} translate",
            "newpath",
            f"{center.x} {center.y} moveto",
            f"1 1 {self._num_sides - 1} " + "{",
            f"    {self._side_length} 0 rlineto",
            f"    {interior_angle} rotate",
            "} for",
            "closepath",
            "stroke",
            "grestore"
        )
