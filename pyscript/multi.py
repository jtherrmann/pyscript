from . import Shape


class MultiShape(Shape):

    def __init__(self, *shapes):
        self._shapes = shapes
