from Point import Point
from Grid import Grid
from DrawPixel import drawPixel_VerticalLine, drawPixel_HorizontalLine, drawPixel_Square

'''线有线宽 —— 线刷子算法'''
def drawLine_with_width_LineBrush(grid, start, end, width):
    dx, dy = (end.x - start.x), (end.y - start.y)
    x, y = start.x, start.y

    if abs(dy) <= abs(dx):

        e = -dx

        for x in range(start.x, end.x):

            drawPixel_HorizontalLine(x, y, 1, grid, width, "line")

            if e > 0:
                e += (dy - dx) << 1
                y += 1
            else:
                e += (dy) << 1
                # y += 0
    else:

        e = -dy

        for y in range(start.y, end.y):

            drawPixel_VerticalLine(x, y, 1, grid, width, "line")

            if e > 0:
                e += (dx - dy) << 1
                x += 1
            else:
                e += (dx) << 1
                # x += 0


'''线有线宽 —— 正方形刷子算法'''
def drawLine_with_width_SquareBrush(grid, start, end, width):
    dx, dy = (end.x - start.x), (end.y - start.y)
    x, y = start.x, start.y

    if abs(dy) <= abs(dx):

        e = -dx

        for x in range(start.x, end.x):

            drawPixel_Square(x, y, 1, grid, width, "line")

            if e > 0:
                e += (dy - dx) << 1
                y += 1
            else:
                e += (dy) << 1
                # y += 0
    else:

        e = -dy

        for y in range(start.y, end.y):

            drawPixel_Square(x, y, 1, grid, width, "line")

            if e > 0:
                e += (dx - dy) << 1
                x += 1
            else:
                e += (dx) << 1
                # x += 0


def main():
    grid = Grid([100, 100])
    start, end = Point(0, 1), Point(50, 70)
    # start, end = Point(0, 1), Point(70, 50)
    width = 10

    # drawLine_with_width_LineBrush(grid, start, end, width)
    drawLine_with_width_SquareBrush(grid, start, end, width)

    # start, end = Point(50, 70), Point(90, 80)
    # drawLine_with_width_LineBrush(grid, start, end, width)

    grid.show()


if __name__ == '__main__':
    main()
