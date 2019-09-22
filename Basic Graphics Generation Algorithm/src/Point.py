'''坐标点类'''
class Point(object):
    def __init__(self, x, y):
        '''

        :param x: 横坐标
        :param y: 纵坐标
        '''
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y