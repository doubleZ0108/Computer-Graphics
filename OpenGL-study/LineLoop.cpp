/*»·Ïß*/
void drawLineLoop()
{
	glColor3f(1.0, 1.0, 1.0);

	glLineWidth(5.0);

	glBegin(GL_LINE_LOOP);
	glVertex3d(0.0f, 0.0f, 0.0f);
	glVertex3d(0.2f, 0.2f, 0.2f);
	glVertex3d(0.2f, 0.5f, 0.0f);
	glVertex3d(0.4f, 0.7f, 0.0f);
	glEnd();
}
