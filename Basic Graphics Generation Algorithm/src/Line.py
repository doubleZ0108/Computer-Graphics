from Point import Point
from Grid import Grid


def drawPixel(x , y, color, grid):
    grid[[y,x]] = color     # 由于pyplot库中纵轴为x，横轴为y；这里人工颠倒一下

'''基础算法'''
def drawLine_Basic(grid, start, end):
    k = (end.y-start.y)/(end.x-start.x)
    b = start.y - k * start.x

    for xi in range(start.x, end.x):    # 栅格的性质
        yi = k * xi + b
        drawPixel(xi, int(yi+0.5), 1, grid)     # y坐标要进行近似

'''数值微分算法（DDA）'''
def drawLine_DDA(grid, start, end):
    k = (end.y - start.y) / (end.x - start.x)
    xi, yi = start.x, start.y

    if abs(k) <= 1:
        for xi in range(start.x, end.x):
            drawPixel(xi, int(yi+0.5), 1, grid)
            yi += k
    else:
        for yi in range(start.y, end.y):
            drawPixel(int(xi+0.5), yi, 1, grid)
            xi += 1/k

'''中点画线法'''
def drwaLine_MidPoint(grid, start, end):
    a, b, c = start.y-end.y, end.x-start.x, start.x*end.y-end.x*start.y

    xp, yp = start.x, start.y
    if abs(end.y - start.y) <= abs(end.x - start.x):
        for xp in range(start.x, end.x):
            drawPixel(xp, yp, 1, grid)

            delta = a*(xp+1) + b*(yp+0.5) + c   # 考核点(xp+1, yp+0.5)
            if delta < 0:
                yp += 1
            else:
                # yp += 0
                pass
    else:
        for yp in range(start.y, end.y):
            drawPixel(xp, yp, 1, grid)

            delta = a*(xp+0.5) + b*(yp+1) + c   # 考核点(xp+0.5, yp+1)

            if delta > 0:
                xp += 1
            else:
                # xp += 0
                pass

'''中点画线法 with DDA'''
def drawLine_MidPoint_with_DDA(grid, start, end):
    a, b = start.y-end.y, end.x-start.x

    d = a + (b<<2)      # 用2d代替d， 摆脱小数


    xp, yp = start.x, start.y
    if abs(end.y - start.y) <= abs(end.x - start.x):

        d1, d2 = a << 2, (a + b) << 2

        for xp in range(start.x, end.x):
            drawPixel(xp, yp, 1, grid)

            if d < 0:
                yp += 1
                d += d2
            else:
                d += d1
    else:

        d1, d2 = b << 2, (a + b) << 2

        for yp in range(start.y, end.y):
            drawPixel(xp, yp, 1, grid)

            if d >   0:
                xp += 1
                d += d2
            else:
                d += d1

'''Bresenham画线法'''
def drawLine_Bresenham(grid, start, end):
    k = (end.y - start.y) / (end.x - start.x)
    x, y = start.x, start.y
    e = -0.5

    if abs(k) <= 1:
        for x in range(start.x, end.x):
            drawPixel(x, y, 1, grid)

            if e > 0:
                e += k - 1
                y += 1
            else:
                e += k
                # y += 0
    else:
        for y in range(start.y, end.y):
            drawPixel(x, y, 1, grid)

            if e > 0:
                e += 1/k -1
                x += 1
            else:
                e += 1/k
                # x += 0

'''Bresenham画线法(去点浮)'''
def drawLine_Bresenham_nonreal(grid, start, end):
    dx, dy = (end.x - start.x), (end.y - start.y)
    x, y = start.x, start.y

    if abs(dy) <= abs(dx):

        e = -dx

        for x in range(start.x, end.x):
            drawPixel(x, y, 1, grid)

            if e > 0:
                e += (dy - dx) << 2
                y += 1
            else:
                e += (dy) << 2
                # y += 0
    else:

        e = -dy

        for y in range(start.y, end.y):
            drawPixel(x, y, 1, grid)

            if e > 0:
                e += (dx - dy) << 2
                x += 1
            else:
                e += (dx) << 2
                # x += 0



def main():
    grid = Grid([100, 100])
    start, end = Point(0, 1), Point(50, 70)
    # start, end = Point(0, 1), Point(70, 50)

    # drawLine_Basic(grid, start, end)
    # drawLine_DDA(grid, start, end)
    # drwaLine_MidPoint(grid, start, end)
    # drawLine_MidPoint_with_DDA(grid, start, end)
    # drawLine_Bresenham(grid, start, end)
    drawLine_Bresenham_nonreal(grid, start, end)

    grid.show()


if __name__=='__main__':
    main()