/*�����*/
void drawPolygon()
{
	glColor3f(0.1, 0.2, 0.3);

	/* ����������������: ����ͷ���
	 * ��Ļ����ʱ�뷽����ֶ���Ķ���γ�Ϊ����
	 */
	glFrontFace(GL_CW);		//˳ʱ�뷽��Ϊ����

	/* GL_POLYGON
	 * ������������Ķ����
	 * Ҫ�����ж��㶼λ��һ��ƽ����, ����εĸ��߲����ཻ
	 */
	glBegin(GL_POLYGON);
	glVertex3d(0.0f, 0.0f, 0.0f);
	glVertex3d(0.2f, 0.5f, 0.0f);
	glVertex3d(0.4f, 0.8f, 0.0f);
	glVertex3d(0.6f, 0.5f, 0.0f);
	glVertex3d(0.3f, 0.0f, 0.0f);
	glEnd();
}
