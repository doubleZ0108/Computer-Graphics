'''在网格中绘制一个像素点'''
def drawPixel(x, y, color, grid):
    grid[[y, x]] = color  # 由于pyplot库中纵轴为x，横轴为y；这里人工颠倒一下


'''绘制对称的8个像素，并进行平移'''
def drawPixel_symmetry8(x, y, color, grid):
    grid[[y + 50, x + 50]] = color
    grid[[x + 50, y + 50]] = color
    grid[[-x + 50, y + 50]] = color
    grid[[-y + 50, x + 50]] = color
    grid[[-y + 50, -x + 50]] = color
    grid[[-x + 50, -y + 50]] = color
    grid[[y + 50, -x + 50]] = color
    grid[[x + 50, -y + 50]] = color


'''绘制对称的4个像素，并进行平移'''
def drawPixel_symmetry4(x, y, color, grid):
    grid[[y + 50, x + 50]] = color
    grid[[-y + 50, x + 50]] = color
    grid[[-y + 50, -x + 50]] = color
    grid[[y + 50, -x + 50]] = color


'''绘制垂直的线宽'''
def drawPixel_VerticalLine(x, y, color, grid, width, type="line"):
    for w in range(-width // 2, width // 2):

        if y + w > -1 and y + w < grid.height:  # 出界检测

            if type == "line":
                drawPixel(x, y + w, 1, grid)
            elif type == "square":
                drawPixel_symmetry8(x, y + w, 1, grid)


'''绘制水平的线宽'''
def drawPixel_HorizontalLine(x, y, color, grid, width, type="line"):
    for w in range(-width // 2, width // 2):

        if x + w > -1 and x + w < grid.width:  # 出界检测

            if type == "line":
                drawPixel(x + w, y, 1, grid)
            elif type == "square":
                drawPixel_symmetry8(x + w, y, 1, grid)


'''绘制正方形的线宽'''
def drawPixel_Square(x, y, color, grid, width, type="line"):
    for a in range(-width // 4, width // 4):
        for b in range(-width // 4, width // 4):

            if x + a > -1 and x + a < grid.width and y + b > -1 and y + b < grid.height:

                if type == "line":
                    drawPixel(x + a, y + b, 1, grid)
                elif type == "square":
                    drawPixel_symmetry8(x + a, y + b, 1, grid)
