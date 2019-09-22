from Point import Point
from Grid import Grid


def drawPixel(x , y, color, grid):
    grid[[x,y]] = color


def drawLine_Basic(grid, start, end):
    k = (end.y-start.y)/(end.x-start.x)
    b = start.y - k * start.x

    for xi in range(start.x, end.x):    # 栅格的性质
        yi = k * xi + b
        drawPixel(xi, int(yi+0.5), 1, grid)     # y坐标要进行近似

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


def main():
    grid = Grid([100, 100])

    start, end = Point(0, 1), Point(50, 70)
    # start, end = Point(0, 1), Point(70, 50)

    # drawLine_Basic(grid, start, end)
    drawLine_DDA(grid, start, end)

    grid.show()


if __name__=='__main__':
    main()