from Point import Point
from Grid import  Grid
from DrawPixel import drawPixel_symmetry8

'''中点画圆法(DDA)(去点浮)'''
def drawArc_MidPoint_with_DDA_nonreal(grid, R, linetype):
    d = 1 - R
    deltax, deltay = 3, 2 - (R << 1)
    counter = 0

    x, y = 0, R
    while x <= y:

        if linetype[counter % len(linetype)]:
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

        counter += 1


def main():
    grid = Grid([100, 100])
    R = 40

    linetype_str = input('请输入0和1组成的字串: ')
    linetype = list(map(int, list(linetype_str)))

    drawArc_MidPoint_with_DDA_nonreal(grid, R, linetype)

    grid.show()


if __name__ == '__main__':
    main()