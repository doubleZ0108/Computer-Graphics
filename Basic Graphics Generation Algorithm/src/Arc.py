from Grid import Grid
from math import sqrt, cos, sin
from DrawPixel import drawPixel, drawPixel_symmetry8, drawPixel_symmetry4

'''暴力方法'''
def drawArc_Basic(grid, R):
    x, y = 0, R
    while x < y:
        drawPixel_symmetry8(x, int(y+0.5), 1, grid)

        x += 1
        y = sqrt(R**2 - x**2)


'''中点画圆法(DDA)'''
def drawArc_MidPoint_with_DDA(grid, R):
    d = 1 - R

    x, y = 0, R
    while x <= y:
        drawPixel_symmetry8(x, y, 1, grid)

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
    deltax, deltay = 3, 2 - (R << 1)

    x, y = 0, R
    while x <= y:
        drawPixel_symmetry8(x, y, 1, grid)

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


'''Bresenham画圆法'''
def drawArc_Bresenham(grid, R):
    delta = (1 - R) << 1

    x, y = 0, R
    while y >= 0:
        drawPixel_symmetry4(x, y, 1, grid)

        if delta < 0:
            delta1 = ((delta + y) << 1) - 1
            if delta1 <= 0:
                direction = 1
            else:
                direction = 2
        elif delta > 0:
            delta2 = ((delta - x) << 1) - 1
            if delta2 <= 0:
                direction = 2
            else:
                direction = 3
        else:
            direction = 2


        if direction == 1:      # 前进到 正右
            x += 1
            delta += (x << 1) + 1
        elif direction == 2:    # 前进到 右下
            x += 1
            y -= 1
            delta += ((x - y) << 1) + 2
        else:                   # 前进到 正下
            y -= 1
            delta += 1 - (y << 1)


'''正负法'''
def drawArc_PositiveNegative(grid, R):
    F = 0

    x, y = 0, R
    while x <= y:
        drawPixel_symmetry8(x, y, 1, grid)
        print(F)
        if F <= 0:
            F += (x << 1) + 1
            x += 1
        else:
            F += 1 - (y << 1)
            y -= 1


'''圆内接正多边形逼近法'''
def drawArc_InscribedRegularPolygonApproximate(grid, R):
    Alpha = 1/R
    cosAlpha, sinAlpha = cos(Alpha), sin(Alpha)

    x, y = R, 0
    while x >= y:
        drawPixel_symmetry8(int(x+0.5), int(y+0.5), 1, grid)

        x = cosAlpha * x - sinAlpha * y
        y = sinAlpha * x + cosAlpha * y


def main():
    grid = Grid([100, 100])
    R = 40

    # drawArc_Basic(grid, R)
    # drawArc_MidPoint_with_DDA(grid, R)
    # drawArc_MidPoint_with_DDA_nonreal(grid, R)
    # drawArc_Bresenham(grid, R)
    # drawArc_PositiveNegative(grid, R)
    drawArc_InscribedRegularPolygonApproximate(grid, R)

    grid.show()


if __name__ == '__main__':
    main()