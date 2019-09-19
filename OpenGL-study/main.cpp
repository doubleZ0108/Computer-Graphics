#include <gl/glut.h>

void Show(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glFlush();
}

int main(int argc, char* argv[])
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_RED | GLUT_SINGLE);
	glutInitWindowPosition(100, 100);
	glutInitWindowSize(600, 600);
	glutCreateWindow("title");
	glutDisplayFunc(Show);
	glutMainLoop();

	return 0;
}