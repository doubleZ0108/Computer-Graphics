# 基本图形生成算法

[TOC]

------

## 直线段

### 基础算法

计算斜率和截距，通过`y = kx + b`的直线表达式计算每一个x对应的y值

```python
def drawLine_Basic(grid, start, end):
  k = (end.y-start.y)/(end.x-start.x)
  b = start.y - k * start.x

  for xi in range(start.x, end.x):    # 栅格的性质
    yi = k * xi + b
    drawPixel(xi, int(yi+0.5), 1, grid)     # y坐标要进行近似
```

------

### 数值微分算法(DDA)

- 采用“增量”的思想

  - 当`|k|<=1`时，x每增加1，y增加k
  - 当`|k|>1`时，y每增加1，x增加1/k

- 证明: (这里只考虑`|k|<=1`当情况)

  由$x_{i+1} = x_{i} + 1$

  $y_{i+1} = k*x_{i+1} + b = k*(x_{i}+1) + b = k*x_{i} + b + k = y_{i} + k$

```python
def drawLine_DDA(grid, start, end):
  k = (end.y - start.y) / (end.x - start.x)
  xi, yi = start.x, start.y

  if(abs(k<=1)):
    for xi in range(start.x, end.x):
      drawPixel(xi, int(yi+0.5), 1, grid)
      yi += k
  else:
    for yi in range(start.y, end.y):
      drawPixel(int(xi+0.5), yi, 1, grid)
      xi += 1/k
```

#### 如果不对k进行分类讨论

![non-classify](ScreenShots/non-classify.png)

<center>不对k进行分类讨论</center>

![classify](ScreenShots/classify.png)

<center>对k进行分类讨论</center>

------

