from . import StackedShapes, Point


class VerticalShapes(StackedShapes):

    def _get_centers(self, center):
        current_y = center.y - self._get_height() / 2
        for shape in self._shapes:
            half_shape_height = shape._get_height() / 2
            current_y += half_shape_height
            yield Point(center.x, current_y)
            current_y += half_shape_height

    def _get_width(self):
        return max((shape._get_width() for shape in self._shapes), default=0)

    def _get_height(self):
        return sum(shape._get_height() for shape in self._shapes)
