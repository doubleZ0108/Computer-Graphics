/*ֱ��*/
void drawLines(void)
{
	glColor3f(1.0, 1.0, 1.0);

	glLineWidth(5.0);			//������Ϊ��λ�����߻��ƵĿ��

	/* ָ������
	 * @param factor: [1,255]֮��,ָ������ģʽ��ÿλ�ĳ���
	 * @param pattern: 16λ����ָ��λģʽ, λ==1ʱҪ��, ==0ʱ����
	 *
	 * ��: pattern == 0x3f07
	 *     �����Ʊ�ʾΪ: 0011 1111 0000 0111
	 *     �ӵ�λ��ʼ(����3������,����5������,����6������,����2������������һ����)
	 *     factor == 2
	 *     ����λ������ֵ����2
	 */
	glLineStipple(1, 0xAAAA);
	glEnable(GL_LINE_STIPPLE);		//�������ͺ������glEnable()���������

	glBegin(GL_LINES);
	glVertex3d(0.0f, 0.0f, 0.0f);
	glVertex3d(0.2f, 0.2f, 0.2f);
	glVertex3d(0.2f, 0.5f, 0.0f);
	glVertex3d(0.4f, 0.7f, 0.0f);
	glEnd();
}
