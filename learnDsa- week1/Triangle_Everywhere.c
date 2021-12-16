#include <stdio.h>
int main()
{
    int a, b, c, flag=0, ans;
    scanf("%d%d%d", &a, &b, &c);
    if (a != 0 && b != 0 && c != 0)
    {
        if (a + b > c && a + c > b && b + c > a)
        {
            flag = 1;
        }
        else
        {
            flag = 0;
        }
    }
    else
    {
        flag = 0;
    }
    if (flag == 0)
    {
        printf("-1");
    }
    else
    {
        if (a == b && b == c)
        {
            printf("1");
        }
        else if (a == b || b == c || c == a)
        {
            printf("2");
        }
        else
        {
            printf("3");
        }
    }
    return 0;
}