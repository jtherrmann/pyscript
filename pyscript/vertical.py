from . import StackedShapes


class VerticalShapes(StackedShapes):

    _variable_coord_name = 'y'

    def _get_width(self):
        return max((shape._get_width() for shape in self._shapes), default=0)

    def _get_height(self):
        return sum(shape._get_height() for shape in self._shapes)
