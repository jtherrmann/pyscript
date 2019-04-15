from . import StackedShapes


class HorizontalShapes(StackedShapes):

    _variable_coord_name = 'x'

    def _get_width(self):
        return sum(shape._get_width() for shape in self._shapes)

    def _get_height(self):
        return max((shape._get_height() for shape in self._shapes), default=0)
