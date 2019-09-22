import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('TkAgg')
import numpy as np


'''坐标平面类'''
class Grid(object):
    def __init__(self, size):
        '''

        :param size: 坐标平面的尺寸
        '''
        self._width = size[0]
        self._height = size[1]
        self._grid = np.zeros([self._width, self._height])

        self.adjust_axis()

    def adjust_axis(self):
        '''调整坐标轴的方向：向右为x轴正方向，向上为y轴正方向'''
        axis = plt.gca()
        axis.set_ylim((0, self._height))
        axis.set_xlim((0, self._width))

    def __setitem__(self, key, value):
        '''这里不太知道二维数组更pro的写法'''
        print(key[0],key[1])
        self._grid[key[0]][key[1]] = value

    def clear(self):
        '''清空坐标平面'''
        self._grid = np.zeros([self._width, self._height])

    def show(self):
        '''绘制平面内的所有图像'''
        plt.imshow(self._grid)
        plt.show()
