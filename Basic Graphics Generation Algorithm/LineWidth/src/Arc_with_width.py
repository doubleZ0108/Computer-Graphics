from Grid import Grid
from DrawPixel import drawPixel_VerticalLine, drawPixel_Square

'''圆有线宽 —— 线刷子算法'''
def drawArc_with_width_LineBrush(grid, R, width):
    d = 1 - R
    deltax, deltay = 3, 2 - (R << 1)

    x, y = 0, R
    while x <= y:

        drawPixel_VerticalLine(x, y, 1, grid, width, "square")

        if d < 0:
            x += 1
            d += deltax
            deltax += 2
        else:
            x += 1
            y -= 1
            d += (deltax + deltay)
            deltax += 2
            deltay += 2


'''圆有线宽 —— 正方形刷子算法'''
def drawArc_with_width_SquareBrush(grid, R, width):
    d = 1 - R
    deltax, deltay = 3, 2 - (R << 1)

    x, y = 0, R
    while x <= y:

        drawPixel_Square(x, y, 1, grid, width, "square")

        if d < 0:
            x += 1
            d += deltax
            deltax += 2
        else:
            x += 1
            y -= 1
            d += (deltax + deltay)
            deltax += 2
            deltay += 2


def main():
    grid = Grid([100, 100])
    R = 40
    width = 10

    # drawArc_with_width_LineBrush(grid, R, width)

    drawArc_with_width_SquareBrush(grid, R, width)

    grid.show()


if __name__ == '__main__':
    main()
