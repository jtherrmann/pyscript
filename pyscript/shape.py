from abc import ABC, abstractmethod

from . import Point


class Shape(ABC):

    def export_postscript(
            self, center=Point(0, 0), show_center=False, filename="shape.ps"):
        postscript_code = self._get_toplevel_postscript(center, show_center)
        with open(filename, "w+") as output_file:
            output_file.write(postscript_code)

    # @abstractmethod # TODO: uncomment
    def width(self):
        pass

    # @abstractmethod # TODO: uncomment
    def height(self):
        pass

    def _get_toplevel_postscript(self, center, show_center):
        postscript_code = self._get_postscript(center) + "\n"

        if show_center:
            postscript_code += self._show_center(center) + "\n"

        return postscript_code + "showpage\n"

    # TODO: check method signature is consistent w/ all subclasses
    @abstractmethod
    def _get_postscript(self, center):
        pass

    @staticmethod
    def _show_center(center):
        return "\n".join((
            "% Show center for debugging purposes.",
            "newpath",
            f"{center.x} {center.y} 2 0 360 arc",
            "fill"
        )) + "\n"

    @staticmethod
    def _join_lines(*lines):
        return "\n".join(lines) + "\n"

    @staticmethod
    def _scaled(self, scale_factor_x, scale_factor_y):
        return self._join_lines(
            "newpath",
            f"{scale_factor_x} ",
            f"{scale_factor_y} ",
            "scale",
            f"{self}"
        )
