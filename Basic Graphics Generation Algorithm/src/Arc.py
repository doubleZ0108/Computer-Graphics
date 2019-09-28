from Point import Point
from Grid import Grid
from math import sqrt
from DrawPixel import drawPixel


def drawArc_Basic(grid, R):
    for x in range(0, R+1):
        y = sqrt(R**2 - x**2)

        drawPixel(x, int(y+0.5), 1, grid)

def main():
    grid = Grid([100, 100])
    R = 80

    drawArc_Basic(grid, R)

    grid.show()


if __name__ == '__main__':
    main()