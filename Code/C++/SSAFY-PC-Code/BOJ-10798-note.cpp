//���� : �����б�
//���� : ���η� ���� �ٸ� ���̷� ������ ���ڵ��� ���η� ���� �� �ִ°�
//ũ�Ⱑ �־����� �ʰ� �־����� ���ڵ��� ������ ������� ������ �Է¹��� �� �ִ°�

/*���̵�� : �̰� ��¿ �� ���� 2���� �迭 �ؾߵǰڴµ�
1. ���� ���̰� ���� �ٸ� 2���� �迭�� �����, erroró���� �����Ѵ�.
or ���� ���̸� ���� �ϵ�,  �峭���� ���� ����(ex -1)�� �ʱ�ȭ�ϰ� �̸� ������ �ǳʶڴ�.
2. ���� ����� �� ����� �� �ϴ� ���� �ϰ���
*/

/*����
1.�׳� 2�����迭�� �����ϸ� �ɽ��ϴ�, 2���� ���͸� �Ẹ��
vector<vector<int>> ���͸�; ���� �����ϸ� ��
2. �Է� ��������, while�� �Ἥ '\n'�� �ν��� �� ���� �о�� �� ��
3. ����Ҷ��� front, pop front ����, empty�� ��� continue �ϴ� ������
*/

//������ : ������ \n�̳� ������ �޾ƿͼ� �����ؾ� �� ���� �ִ�. �׷��� scanf
#include <iostream>
#include <vector>
using namespace std;

vector<vector<char>> board(5);

int main()
{
	//2�������� �ޱ�
	for (int i = 0; i<5;++i)
		while (1)
		{
			char temp;
			scanf("%c", &temp); //cin ���� ���� �����ϹǷ� �ȵ�
			if (temp == '\n') break;
			board[i].push_back(temp);
		}
	
	//2�������� ���η� ���
	for(int j = 0; j<15;++j)
		for (int i = 0; i < 5; ++i)
		{
			if (board[i].empty()) continue;
			cout << board[i].front();
			board[i].erase(board[i].begin());
		}
	
}


