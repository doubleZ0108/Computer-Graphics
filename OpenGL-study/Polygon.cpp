/*多边形*/
void drawPolygon()
{
	glColor3f(0.1, 0.2, 0.3);

	/* 多边形由两个面组成: 正面和反面
	 * 屏幕上逆时针方向出现顶点的多边形成为正面
	 */
	glFrontFace(GL_CW);		//顺时针方向为正面

	/* GL_POLYGON
	 * 绘制任意边数的多边形
	 * 要求所有顶点都位于一个平面内, 多边形的各边不能相交
	 */
	glBegin(GL_POLYGON);
	glVertex3d(0.0f, 0.0f, 0.0f);
	glVertex3d(0.2f, 0.5f, 0.0f);
	glVertex3d(0.4f, 0.8f, 0.0f);
	glVertex3d(0.6f, 0.5f, 0.0f);
	glVertex3d(0.3f, 0.0f, 0.0f);
	glEnd();
}
