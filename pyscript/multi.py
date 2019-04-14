from abc import abstractmethod

from . import Shape


class MultiShape(Shape):

    def _get_postscript(self, center):
        return "\n".join(self._get_each_component_postscript(center))

    @abstractmethod
    def _get_each_component_postscript(self, center):
        pass

    def __init__(self, *shapes):
        self._shapes = shapes
