#include<stdio.h>
#include<stdlib.h>
int main()
{
    long int n,k,j,count=0;
    scanf("%ld%ld",&n,&k);
    for(int i=0;i<n;i++){
        scanf("%ld",&j);
        if(j%k==0){
            count++;
        }
        
    }
    printf("%ld",count);
    return 0;
}