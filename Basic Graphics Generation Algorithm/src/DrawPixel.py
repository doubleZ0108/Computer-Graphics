'''在网格中绘制像素'''
def drawPixel(x , y, color, grid):
    grid[[y,x]] = color     # 由于pyplot库中纵轴为x，横轴为y；这里人工颠倒一下
