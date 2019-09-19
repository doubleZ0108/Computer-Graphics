/*点*/
void drawPoints(void)
{
	glColor3f(1.0, 1.0, 1.0);

	glPointSize(5);			//以像素为单位控制点的大小

	glBegin(GL_POINTS);
	glVertex3d(0.0, 0.0, 0.0);
	glEnd();
}
