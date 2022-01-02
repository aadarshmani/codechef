#include <stdio.h>
#include <stdlib.h>
int compare (const void * a, const void * b)
{
  int data1 = *(int *)a, data2 = *(int *)b;
  if(data1 < data2) // a < b
    return -1;
  else if(data1 == data2) // a == b
    return 0;
  else 
    return 1;  // a > b
}
int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        long int n,a[1000],ans,size,median;
        scanf("%ld",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%ld",&a[i]);
        }
        size=n;
        qsort((void*)a, size, sizeof(long int), compare);
        median=(n)/2;
        ans=a[median]-a[median-1];

    printf("%ld\n",ans);
    }   
    return 0;
}