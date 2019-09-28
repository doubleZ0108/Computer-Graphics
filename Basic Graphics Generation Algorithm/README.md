# 基本图形生成算法

[TOC]

------

## 直线段

### 基础算法

计算斜率和截距，通过`y = kx + b`的直线表达式计算每一个x对应的y值

```python
'''基础算法'''
def drawLine_Basic(grid, start, end):
  k = (end.y-start.y)/(end.x-start.x)
  b = start.y - k * start.x

  for xi in range(start.x, end.x):    # 栅格的性质
    yi = k * xi + b
    drawPixel(xi, int(yi+0.5), 1, grid)     # y坐标要进行近似
```

<img src="ScreenShots/Line/Basic1.png" alt="Basic1" style="zoom:50%;" />

<img src="ScreenShots/Line/Basic2.png" alt="Basic2" style="zoom:50%;" />

------

### 数值微分算法(DDA)

- 采用“增量”的思想

  - 当`|k|<=1`时，x每增加1，y增加k
  - 当`|k|>1`时，y每增加1，x增加1/k

- 证明: (这里只考虑`|k|<=1`当情况)

  由$x_{i+1} = x_{i} + 1$

  $y_{i+1} = k*x_{i+1} + b = k*(x_{i}+1) + b = k*x_{i} + b + k = y_{i} + k$

```python
'''数值微分算法（DDA）'''
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

<img src="ScreenShots/Line/DDA1.png" alt="DDA1" style="zoom:50%;" />

<img src="ScreenShots/Line/DDA2.png" alt="DDA2" style="zoom:50%;" />

#### 如果不对k进行分类讨论

<img src="ScreenShots/Line/non-classify.png" alt="non-classify" style="zoom:72%;" />

<center>不对k进行分类讨论</center>
<img src="ScreenShots/Line/classify.png" alt="classify" style="zoom:72%;" />

<center>对k进行分类讨论</center>
------

### 中点画线法

- 设直线方程为：ax + by + c =0

  - a = y0 - y1
  - b = x1 - x0
  - c = x0y1 - x1y0

- 考核点：(xp+1, yp+0.5)

- 判别式：$\Delta$ = F(xp+1, yp+0.5) = a*(xp+1) + b*(yp+0.5) + c

  - 如果$\Delta$<0 => Q点在M下方 => 选p2

  - else， 选p1

    <img src="ScreenShots/Line/MidPoint_principle.jpeg" alt="MidPoint_principle" style="zoom:50%;" />

```python
'''中点画线法(k<=1)'''
def drwaLine_MidPoint(grid, start, end):
  a, b, c = start.y-end.y, end.x-start.x, start.x*end.y-end.x*start.y

  xp, yp = start.x, start.y
  for xp in range(start.x, end.x):
    drawPixel(xp, yp, 1, grid)

    delta = a*(xp+1) + b*(yp+0.5) + c   # 考核点(xp+1, yp+0.5)
    if delta<0:
      yp += 1
    else:
      # yp += 0
      pass
```

<img src="ScreenShots/Line/MidPoint1.png" alt="MidPoint1" style="zoom:50%;" />

<img src="ScreenShots/Line/MidPoint2.png" alt="MidPoint2" style="zoom:50%;" />

#### 在中点画线法中添加增量的思想

- 若取p1，增量为a
- 若取p2，增量为a+b
- 初值：d0 = a + 0.5b
- 由于只用d的符号来判断，可以用2d代替d，摆脱浮点数

```python
'''中点画线法 with DDA'''
def drawLine_MidPoint_with_DDA(grid, start, end):
  a, b = start.y-end.y, end.x-start.x

  d = a + (b<<2)      # 用2d代替d， 摆脱小数
  d1, d2 = a<<2, (a+b)<<2

  xp, yp = start.x, start.y
  for xp in range(start.x, end.x):
    drawPixel(xp, yp, 1, grid)

    if d<0:
      yp += 1
      d += d2
    else:
      d += d1
```

<img src="ScreenShots/Line/MidPoint_with_DDA1.png" alt="MidPoint_with_DDA1" style="zoom:50%;" />

<img src="ScreenShots/Line/MidPoint_with_DDA2.png" alt="MidPoint_with_DDA2" style="zoom:50%;" />

------

### Bresenham画线法

- 由误差项符号决定下一个像素选正右方还是右上方
- 判别式：$\varepsilon = y_{i+1} - y_{i,r} - 0.5$
  - $\varepsilon > 0$, 取右上
  - else，取正右
- 引入增量思想：
  - $\varepsilon > 0$，增量为 k-1
  - else，增量为 k
  - 初始值：-0.5

```python
'''Bresenham画线法(k<=1)'''
def drawLine_Bresenham(grid, start, end):
  k = (end.y - start.y) / (end.x - start.x)
  x, y = start.x, start.y
  e = -0.5

  for x in range(start.x, end.x):
    drawPixel(x, y, 1, grid)

    if e > 0:
      e += k - 1
      y += 1
    else:
      e += k
      # y += 0
```

<img src="ScreenShots/Line/Bresenham1.png" alt="Bresenham1" style="zoom:50%;" />

<img src="ScreenShots/Line/Bresenham2.png" alt="Bresenham2" style="zoom:50%;" />

#### 去点浮

- 用$\varepsilon' = 2 * \varepsilon * dx$代替$\varepsilon$
- 去掉k的计算
- 增量：
  - $\varepsilon > 0$，增量为 2(dy - dx)
  - else，增量为 2dy
  - 初始值：-dx

```python
'''Bresenham画线法(去点浮)(k<=1)'''
def drawLine_Bresenham_nonreal(grid, start, end):
    dx, dy = (end.x - start.x), (end.y - start.y)
    x, y = start.x, start.y
    e = -dx

    for x in range(start.x, end.x):
      drawPixel(x, y, 1, grid)

      if e > 0:
        e += (dy - dx) << 2
        y += 1
      else:
        e += (dy) << 2
        # y += 0
```

<img src="ScreenShots/Line/Bresenham_nonreal2.png" alt="Bresenham_nonreal2" style="zoom:50%;" />

<img src="ScreenShots/Line/Bresenham_nonreal1.png" alt="Bresenham_nonreal1" style="zoom:50%;" />