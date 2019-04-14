from abc import abstractmethod

from . import Shape


class MultiShape(Shape):

    def __init__(self, *shapes):
        self._shapes = shapes

    def _get_postscript(self, center):
        return "\n".join(self._get_each_component_postscript(center))

    @abstractmethod
    def _get_each_component_postscript(self, center):
        pass


class StackedShapes(MultiShape):

    def _get_each_component_postscript(self, center):
        return (
            shape._get_postscript(center)
            for shape, center in zip(self._shapes, self._get_centers(center))
        )

    @abstractmethod
    def _get_centers(self, center):
        pass
