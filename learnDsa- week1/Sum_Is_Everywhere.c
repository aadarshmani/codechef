#include <stdio.h>
int main()
{
    int n; long long odd = 0, even = 0;
    scanf("%d", &n);
    for (int j = 1; j < 2 * n + 1; j++)
    {
        if (j % 2 == 0)
        {
            even += j;
        }
        else
            odd += j;
    }

    printf("%lld %lld", odd, even);

    return 0;
}