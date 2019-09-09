# 图形学实验: 生成中间帧

🐱变🐯

[TOC]

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

