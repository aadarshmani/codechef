#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        long int n,a[300000]={0};
        long long int ans;
        scanf("%ld",&n);
        for(int i=0;i<n;i++){
            scanf("%ld", &a[i]);
        }
        qsort(a, n, sizeof(long int), cmpfunc);
        ans=(a[n-1]-a[0])*a[n-2];
    printf("%lld\n",ans);
    }   
    return 0;
}