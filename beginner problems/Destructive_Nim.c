#include <stdio.h>
#include<limits.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        long int n,a[1001],secsmall=INT_MAX,temp=0,small=INT_MAX,sum=0,secnum=0,ans;
        scanf("%ld",&n);
        for(int i=0;i<n;i++){
        scanf("%ld",&temp);
        if(temp<small){
            secsmall=small;
            small=temp;
        }
        }
        if((n-2)%2==1){
            sum=1;
        }
        else
        sum=0;
        if(secsmall==1){
            secnum=1;
        }
        else
        secnum=2;
        ans=sum+secnum+1;
        if(ans%2==0){
            printf("ASHISH\n");
        }
        else 
        printf("UTKARSH\n");
        }   
    return 0;
}