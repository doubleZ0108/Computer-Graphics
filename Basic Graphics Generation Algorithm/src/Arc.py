from Point import Point
from Grid import Grid
from math import sqrt
from DrawPixel import drawPixel, drawPixel_symmetry

'''暴力方法'''
def drawArc_Basic(grid, R):
    x, y = 0, R
    while x < y:
        drawPixel_symmetry(x, int(y+0.5), 1, grid)

        x += 1
        y = sqrt(R**2 - x**2)


'''中点画圆法(DDA)'''
def drawArc_MidPoint_with_DDA(grid, R):
    d = 1 - R

    x, y = 0, R
    while x < y:
        drawPixel_symmetry(x, y, 1, grid)

        if d < 0:
            x += 1
            d += 2*x + 3
        else:
            x += 1
            y -= 1
            d += ((x-y) << 1) + 5


'''中点画圆法(DDA)(去点浮)'''
def drawArc_MidPoint_with_DDA_nonreal(grid, R):
    d = 1 - R
    deltax, deltay = 3, 2 - ((R)<<1)

    x, y = 0, R
    while x < y:
        drawPixel_symmetry(x, y, 1, grid)

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

    # drawArc_Basic(grid, R)
    # drawArc_MidPoint_with_DDA(grid, R)
    drawArc_MidPoint_with_DDA_nonreal(grid, R)

    grid.show()


if __name__ == '__main__':
    main()