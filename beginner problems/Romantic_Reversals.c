#include <stdio.h>
#include <string.h>
int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n, k;
        char s[1000001],s1[1000001]="Z";
        scanf("%d %d", &n,&k);
        scanf("%s",s);
        strcat(s1,s);

        

        if (k % 2 == 1)
        {
            printf("%c", s1[k / 2+1]);
            for (int x = 1; x <= k / 2; x++)
            {
                printf("%c", s1[(k / 2+1) + x]);
                printf("%c", s1[(k / 2+1) - x]);
            }
        }
        else
        {
            printf("%c", s1[k / 2+1]);
            for (int x = 1; x <= k / 2-1; x++)
            {
                printf("%c", s1[(k / 2+1) - x]);
                printf("%c", s1[(k / 2+1) + x]);
            }
            printf("%c", s1[1]);
        }
        if(n>k){
        for(int j=k+1;j<n+1;j++){
            printf("%c", s1[j]);
        }
        }
        printf("\n");
    }
    return 0;
}