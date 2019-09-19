/*直线*/
void drawLines(void)
{
	glColor3f(1.0, 1.0, 1.0);

	glLineWidth(5.0);			//以像素为单位控制线绘制的宽度

	/* 指定线型
	 * @param factor: [1,255]之间,指定线型模式中每位的乘数
	 * @param pattern: 16位整数指定位模式, 位==1时要绘, ==0时不绘
	 *
	 * 例: pattern == 0x3f07
	 *     二进制表示为: 0011 1111 0000 0111
	 *     从低位开始(绘制3个像素,不绘5个像素,绘制6个像素,不绘2个像素来连成一条线)
	 *     factor == 2
	 *     各个位置像素值乘上2
	 */
	glLineStipple(1, 0xAAAA);
	glEnable(GL_LINE_STIPPLE);		//定义线型后必须用glEnable()命令激活线型

	glBegin(GL_LINES);
	glVertex3d(0.0f, 0.0f, 0.0f);
	glVertex3d(0.2f, 0.2f, 0.2f);
	glVertex3d(0.2f, 0.5f, 0.0f);
	glVertex3d(0.4f, 0.7f, 0.0f);
	glEnd();
}
