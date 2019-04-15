from abc import abstractmethod

from . import Shape, Point


class MultiShape(Shape):

    def __init__(self, *shapes):
        self._shapes = shapes

    def _get_postscript(self, center):
        return "\n".join(self._get_each_component_postscript(center))

    @abstractmethod
    def _get_each_component_postscript(self, center):
        pass


class StackedShapes(MultiShape):

    def __init__(self, *args, **kwargs):
        if self._variable_coord_name == 'x':
            self._constant_coord_name = 'y'
            self._long_dimension_method = self._get_width.__name__
        elif self._variable_coord_name == 'y':
            self._constant_coord_name = 'x'
            self._long_dimension_method = self._get_height.__name__
        else:
            raise ValueError()

        super().__init__(*args, **kwargs)

    def _get_each_component_postscript(self, center):
        constant_coord = self._get_constant_coord(center)

        variable_coord_start = self._get_variable_coord(center)
        variable_coord = variable_coord_start - self._get_half_long_dimension()

        for shape in self._shapes:
            half_shape_dimension = shape._get_half_dimension(
                self._long_dimension_method
            )
            variable_coord += half_shape_dimension
            yield shape._get_postscript(
                Point(**{self._constant_coord_name: constant_coord,
                         self._variable_coord_name: variable_coord})
            )
            variable_coord += half_shape_dimension

    def _get_half_long_dimension(self):
        return self._get_half_dimension(self._long_dimension_method)

    def _get_constant_coord(self, center):
        return getattr(center, self._constant_coord_name)

    def _get_variable_coord(self, center):
        return getattr(center, self._variable_coord_name)
