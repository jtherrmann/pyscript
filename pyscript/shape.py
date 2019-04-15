from abc import ABC, abstractmethod

from . import Point


class Shape(ABC):

    def export_postscript(
            self, center=Point(0, 0), show_center=False, filename="shape.ps"):
        postscript_code = self._get_toplevel_postscript(center, show_center)
        with open(filename, "w+") as output_file:
            output_file.write(postscript_code)

    def _get_toplevel_postscript(self, center, show_center):
        postscript_code = self._get_postscript(center) + "\n"

        if show_center:
            postscript_code += self._show_center(center) + "\n"

        return postscript_code + "showpage\n"

    def _get_half_dimension(self, dimension_method):
        if dimension_method not in (
                self._get_width.__name__, self._get_height.__name__):
            raise ValueError()
        return getattr(self, dimension_method)() / 2

    @abstractmethod
    def _get_postscript(self, center):
        pass

    @abstractmethod
    def _get_width(self):
        pass

    @abstractmethod
    def _get_height(self):
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
