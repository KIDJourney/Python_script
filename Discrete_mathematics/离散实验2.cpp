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

        cout << "R1 与 R2 的复合关系如下：\n";
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
    cout << "请输入两个关系矩阵，3行3列，仅限输入0和1\n";

}
