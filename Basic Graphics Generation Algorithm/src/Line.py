from Point import Point
from Grid import Grid


def drawPixel(x , y, color, grid):
    grid[[x,y]] = color


def drawLine_Basic(grid, start, end):
    k = (end.y-start.y)/(end.x-start.x)
    b = start.y - k * start.x

    for xi in range(start.x, end.x):
        yi = k * xi + b
        drawPixel(xi, int(yi+0.5), 1, grid)


def main():
    grid = Grid([1000, 1000])

    start, end = Point(0, 1), Point(500, 700)

    drawLine_Basic(grid, start, end)

    grid.show()


if __name__=='__main__':
    main()