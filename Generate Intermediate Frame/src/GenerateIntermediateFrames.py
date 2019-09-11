import os
import shutil
import cv2
import numpy as np
from src.FrameHandler import FrameHandler
from src.myImage2Gif import myImage2Gif

from time import time



'''读取原始图片'''
def readOriginImg(path_cat, path_tiger):
    I_cat = cv2.imread(path_cat)
    I_tiger = cv2.imread(path_tiger)

    return I_cat, I_tiger


'''生成中间帧'''
def generateFrame(I_cat, I_tiger, N):
    # 取两图片最大的长宽作为目标图片的长宽
    width, height = max(I_cat.shape[0], I_tiger.shape[0]), max(I_cat.shape[1], I_tiger.shape[1])
    I_cat = np.resize(I_cat, (width, height, 3))
    I_tiger = np.resize(I_tiger, (width, height, 3))

    # 线性插值公式
    '''
    # 直接使用三维数组
    # 构建 (N+2) * width * height 三纬结果矩阵
    result_frames = [[[0 for _ in range(width)] for _ in range(height)] for _ in range(N + 2)]

    for k in range(0, N + 2):  # 帧循环

        t = k / (1 + N)

        # 对二维图片矩阵遍历
        for x in range(width):
            for y in range(height):
                result_frames[k][x][y] = (1 - t) * I_cat[x][y] + t * I_tiger[x][y]  # 对于图片矩阵中的每一个像素进行数值运算
    '''

    '''
    # 使用numpy数组
    '''
    # 图片的shape是[width, height, 3] -> 构建 (N + 2, width, height, 3)
    result_frames = np.zeros((N + 2, width, height, 3))
    for k in range(0, N + 2):
        t = k / (1 + N)
        result_frames[k] = (1 - t) * I_cat + t * I_tiger        # 直接对于图片矩阵进行矩阵运算

    return result_frames


'''创建结果帧目录'''
def makeResultDir(path_result):
    if os.path.exists(path_result):
        shutil.rmtree(path_result)

    os.mkdir(path_result)


'''将矩阵写出成图片'''
def writeResultFrames(result_frames, dirname, multi_thread=False):
    for index, frame in enumerate(result_frames):
        filename = 'frame' + str(index) + '.png'

        if multi_thread:
            frame_thread = FrameHandler(dirname, filename, frame)
            frame_thread.start()
            frame_thread.join()
        else:
            cv2.imwrite(dirname + filename, np.float32(frame))



def main():
    path_origin = '../Resources/Origin/'
    path_result = '../Resources/Result/'

    '''测试用例1'''
    path_cat = path_origin + 'cat.png'
    path_tiger = path_origin + 'tiger.png'
    '''测试用例2'''
    # path_cat = path_origin + 'her1.jpeg'
    # path_tiger = path_origin + 'her2.jpeg'

    N = int(input('Please input the intermediate frames you want to generate: '))

    # 读取原始图片
    I_cat, I_tiger = readOriginImg(path_cat, path_tiger)

    # 创建结果文件夹储存结果图片
    makeResultDir(path_result)

    # 生成指定数量的中间帧
    result_frames = generateFrame(I_cat, I_tiger, N)

    # 将结果矩阵写出成图片
    writeResultFrames(result_frames, path_result, multi_thread=False)

    # 将帧图片保存为Gif
    myImage2Gif(path_result)



if __name__=='__main__':
    main()