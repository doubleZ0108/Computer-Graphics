/*��*/
void drawPoints(void)
{
	glColor3f(1.0, 1.0, 1.0);

	glPointSize(5);			//������Ϊ��λ���Ƶ�Ĵ�С

	glBegin(GL_POINTS);
	glVertex3d(0.0, 0.0, 0.0);
	glEnd();
}
