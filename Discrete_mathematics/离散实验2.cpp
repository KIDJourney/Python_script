#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
const int Max = 3;
void print_menu();
int main()
{   //freopen("Untitled1.txt","r",stdin);
    int R1[Max][Max];
    int R2[Max][Max];
    int R3[Max][Max];
    while(true)
    {
        print_menu();
        for(int i = 0 ; i < Max;i++)
            memset(R3[i],0,sizeof(R3[i]));
        for(int i = 0 ; i < Max; i++)
            for(int j = 0 ; j < Max ; j++)
                cin >> R1[i][j];
        for(int i = 0 ; i < Max; i++)
            for(int j = 0 ; j < Max ; j++)
                cin >> R2[i][j];
        for(int i = 0 ; i < Max; i++)
        {

            for(int j = 0 ; j < Max; j++)
            {
                for(int k = 0 ; k < Max ; k++)
                {
                    R3[i][j] |=R1[j][k] && R2[k][j];
                }
            }
        }

        cout << "R1 �� R2 �ĸ��Ϲ�ϵ���£�\n";
        for(int i = 0 ; i < Max ;i++)
        {
            for(int j = 0 ; j < Max ; j++)
            {
                cout << R3[i][j];
                (j == Max - 1) ?
                    cout << endl:
                    cout << "   ";
            }
        }

    }
    return 0;
}
void print_menu()
{
    cout << "������������ϵ����3��3�У���������0��1\n";

}
