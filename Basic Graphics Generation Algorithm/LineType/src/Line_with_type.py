from Point import Point
from Grid import Grid
from DrawPixel import drawPixel

def drawLine_with_type(grid, start, end, linetype):
    dx, dy = (end.x - start.x), (end.y - start.y)
    x, y = start.x, start.y

    counter = 0

    if abs(dy) <= abs(dx):

        e = -dx

        for x in range(start.x, end.x):

            if linetype[counter % len(linetype)]:
                drawPixel(x, y, 1, grid)


            if e > 0:
                e += (dy - dx) << 1
                y += 1
            else:
                e += (dy) << 1
                # y += 0

            counter += 1
    else:

        e = -dy

        for y in range(start.y, end.y):

            if linetype[counter % len(linetype)]:
                drawPixel(x, y, 1, grid)

            if e > 0:
                e += (dx - dy) << 1
                x += 1
            else:
                e += (dx) << 1
                # x += 0

            counter += 1

def main():
    grid = Grid([100, 100])
    # start, end = Point(0, 1), Point(50, 70)
    start, end = Point(0, 1), Point(70, 50)

    linetype_str = input('请输入0和1组成的字串: ')
    # linetype_str = "111100"
    linetype = list(map(int, list(linetype_str)))
    drawLine_with_type(grid, start, end, linetype)


    grid.show()


if __name__ == '__main__':
    main()