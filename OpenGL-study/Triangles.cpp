/*Èý½ÇÐÎ*/
void drawTriangles()
{
	glColor3f(0.8, 0.4, 0.3);

	glBegin(GL_TRIANGLES);
	glVertex3d(0.0f, 0.0f, 0.0f);
	glVertex3d(0.5f, 0.5f, 0.0f);
	glVertex3d(0.5f, 0.0f, 0.0f);

	glVertex3d(0.5f, 0.0f, 0.0f);
	glVertex3d(1.0f, 0.5f, 0.0f);
	glVertex3d(1.0f, 0.0f, 0.0f);
	glEnd();
}
