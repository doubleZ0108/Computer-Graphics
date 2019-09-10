# 图形学实验: 生成中间帧

给定初始图片和结束图片，生成中间的N帧，使得首尾自然过渡

[TOC]



------

## 开发环境

- **开发环境：**macOS Mojave 10.14.6
- **开发软件：**PyCharm 2019.1.3
- **开发语言：**python

------

## 如何运行

- 将项目文件夹拷贝到本地环境
- 运行`src/GenerateIntermediateFrames.py`
- 在`Resources/Result/`目录下可查看到生成的中间帧图片
  - `framexx.png`: 为中间帧图片，其中xx为该帧编号
  - `result.gif`: 为该文件夹中所有帧图片生成的gif图片(方便观察处理结果)
- ***可使用自定义图片替换`Resources/Origin/`目录下的原始图片；并且请修改`src/GenerateIntermediateFrames.py ` -> `main()`函数中`path_cat`和`path_tiger`的路径***

------

## 具体实现

### 读取图片

使用`cv2.imread()`将图片读取成矩阵

```python
'''读取原始图片'''
def readOriginImg(path_cat, path_tiger):
  I_cat = cv2.imread(path_cat)
  I_tiger = cv2.imread(path_tiger)

  return I_cat, I_tiger
```

```python
# 读取的图片数据结构
[[[255 255 255]
  [255 255 255]
  [255 255 255]
  ...
  ...
  [ 84 103 112]
  [103 122 128]
  [167 178 181]]]
```

### 生成中间帧(线性插值算法)

- 取两图片最大的长宽作为目标图片的长宽

  ```python
  # 取两图片最大的长宽作为目标图片的长宽
  width, height = max(I_cat.shape[0], I_tiger.shape[0]), max(I_cat.shape[1], I_tiger.shape[1])
  ```

#### 直接使用三维数组

- 构建 (N+2) * width * height 三纬结果矩阵

  ```python
  result_frames = [[[0 for _ in range(width)] for _ in range(height)] for _ in range(N+2)]
  ```

- 使用三重循环进行中间帧生成

  ```python
  for k in range(0, N+2):         # 帧循环
  
    t = k/(1+N)
  
    # 对二维图片矩阵遍历
    for x in range(width):
      for y in range(height):
        result_frames[k][x][y] = (1-t)*I_cat[x][y] + t*I_tiger[x][y]    # 线性插值公式
  ```

#### 使用numpy数组

### 将矩阵写出成图片

```python
'''将矩阵写出成图片'''
def writeResultFrames(result_frames, dirname, multi_thread=False):
  for index, frame in enumerate(result_frames):
    filename = 'frame' + str(index) + '.png'
```

#### 直接写出

```python
else:
  cv2.imwrite(dirname + filename, np.float32(frame))
```

#### 使用多线程处理复杂任务

```python
'''将矩阵保存成图片 - 线程类'''
class FrameHandler(Thread):
  def __init__(self, dirname, filename, frame):
    super().__init__()
    self._dirname = dirname
    self._filename = filename
    self._frame = frame

    def run(self):
      imwrite(self._dirname+self._filename, np.float32(self._frame))
```

```python
if multi_thread:
  frame_thread = FrameHandler(dirname, filename, frame)
  frame_thread.start()
  frame_thread.join()
```

### 将一组帧图片保存为Gif

- 对结果目录中的所有文件进行过滤(只读入生成的中间帧)
- 对读入的中间帧按照先后进行排序
- 调用`image.mimsave()`方法将一组帧图片保存为Gif

```python
'''
Resources/Result/目录下有多张图片
图片格式: framexx.png
'''
import os
import imageio

def myImage2Gif(dirname):
  frames = list(filter(lambda x: x[0:5] == 'frame' and x[-4:] == '.png', os.listdir(dirname)))  # 将不符合命名要求的图片过滤掉(MacOS)会默认创建一些文件
  frames.sort(key=lambda x: int(x[5:-4]))     # 按照图片编号进行排序

  imgs = []
  for frame in frames:
    imgs.append(imageio.imread(dirname+frame))
    imageio.mimsave(dirname+'result.gif', imgs, 'GIF', duration=0.35)
```

------

## 实验分析

### 使用普通三维数组和numpy数组的效率差异



### 使用多线程的效率提升



------

## 遇到的问题

### python构建三维数组



### 将一组帧图片保存为Gif



------

## 项目结构

```
├── README.md
├── Resources
│   ├── Origin
│   │   ├── cat.png
│   │   └── tiger.png
│   └── Result
│       └── result.gif
└── src
    ├── FrameHandler.py
    ├── GenerateIntermediateFrames.py
    └── myImage2Gif.py
```

------

## 关于作者

| 项目     | 信息                |
| -------- | ------------------- |
| 姓名     | 张喆                |
| 学号     | 1754060             |
| 指导老师 | 贾金原老师          |
| 上课时间 | 周一 5、6、7节      |
| 联系方式 | doubleZ0108@163.com |

