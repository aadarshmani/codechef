#include <stdio.h>
int main()
{
    int n,ans,temp=0,flag=0;
    scanf("%d",&n);
    if(n%2==1){flag=1;}
    for(int k=0;k<n/2;k++){
        for(int i=1;i<6;i++){
            printf("%d ",temp+i);
        }
        printf("\n");
        if(flag=1){if(k==(n/2)){
            break;
        }

        }
        for(int j=10;j>5;j--){
            printf("%d ",temp+j);
        }
        printf("\n");
        temp+=10;
    }
    
    return 0;
}