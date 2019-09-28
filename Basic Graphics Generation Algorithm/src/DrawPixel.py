'''在网格中绘制一个像素点'''
def drawPixel(x , y, color, grid):
    grid[[y,x]] = color     # 由于pyplot库中纵轴为x，横轴为y；这里人工颠倒一下


'''绘制对称的8个像素，并进行平移'''
def drawPixel_symmetry8(x, y, color, grid):
    grid[[y+50, x+50]] = color
    grid[[x+50, y+50]] = color
    grid[[-x+50, y+50]] = color
    grid[[-y+50, x+50]] = color
    grid[[-y+50, -x+50]] = color
    grid[[-x+50, -y+50]] = color
    grid[[y+50, -x+50]] = color
    grid[[x+50, -y+50]] = color


'''绘制对称的4个像素，并进行平移'''
def drawPixel_symmetry4(x, y, color, grid):
    grid[[y+50, x+50]] = color
    grid[[-y+50, x+50]] = color
    grid[[-y+50, -x+50]] = color
    grid[[y+50, -x+50]] = color