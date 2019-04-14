from . import MultiShape, Point


class HorizontalShapes(MultiShape):

    def _get_each_component_postscript(self, center):
        current_x = center.x - self._get_width() / 2
        for shape in self._shapes:
            half_shape_width = shape._get_width() / 2
            current_x += half_shape_width
            yield shape._get_postscript(Point(current_x, center.y))
            current_x += half_shape_width

    def _get_width(self):
        return sum(shape._get_width() for shape in self._shapes)

    def _get_height(self):
        return max((shape._get_height() for shape in self._shapes), default=0)
