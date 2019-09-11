'''
Resources/Result/目录下有多张图片
图片格式: framexx.png
'''
import os
from PIL import Image


def myImage2Gif(dirname):
    frames = list(filter(lambda x: x[0:5] == 'frame' and x[-4:] == '.png', os.listdir(dirname)))  # 将不符合命名要求的图片过滤掉(MacOS)会默认创建一些文件
    frames.sort(key=lambda x: int(x[5:-4]))  # 按照图片编号进行排序

    imgs = []
    for frame in frames:
        img = Image.open(dirname + frame)
        imgs.append(img)

    imgs[0].save(dirname + 'result.gif', save_all=True, append_images=imgs, duration=300)


if __name__ == '__main__':

    dirname = '../Resources/Result/'
    myImage2Gif(dirname)