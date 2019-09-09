from cv2 import imwrite
from threading import Thread
import numpy as np


'''将矩阵保存成图片 - 线程类'''
class FrameHandler(Thread):
  def __init__(self, dirname, filename, frame):
    super().__init__()
    self._dirname = dirname
    self._filename = filename
    self._frame = frame

  def run(self):
    imwrite(self._dirname+self._filename, np.float32(self._frame))