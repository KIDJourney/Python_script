#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int Max=100;
void print_menu();
int main()
{
    freopen("in.txt","r",stdin);
    cout<<"请输入矩阵边长"<<endl;
    int R1[Max][Max];
    int R2[Max][Max];
    int R3[Max][Max];
    int x=0;
    while(cin>>x)
    {
        cout<<"请输入两个矩阵"<<endl;
        memset(R3,0,sizeof(R3));
        for(int i = 0 ; i < x; i++)
            for(int j = 0 ; j < x ; j++)
                cin >> R1[i][j];
        for(int i = 0 ; i < x; i++)
            for(int j = 0 ; j < x ; j++)
                cin >> R2[i][j];

        for(int i = 0 ; i < x; i++)
        {

            for(int j = 0 ; j < x; j++)
            {
                int flag=0;
                for(int k = 0 ; k < x ; k++)
                {
                    flag+=R1[i][k] && R2[k][j];
                }
                R3[i][j]=flag;
            }
        }

        cout << "----------------------\n";
        for(int i = 0 ; i < x ; i++)
        {
            for(int j = 0 ; j < x ; j++)
            {
                cout << R3[i][j];
                (j == x - 1) ?cout << endl:cout <<" ";
            }
        }
        cout<<"请输入矩阵边长"<<endl;
    }
    return 0;
}
