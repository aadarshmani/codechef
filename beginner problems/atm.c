#include<stdio.h>
#include<stdlib.h>
int main()
{   
    int wamt; float fbal, ibal;
    scanf("%d %f",&wamt,&ibal);
    if((wamt+0.5)<ibal && wamt%5==0){
        fbal = ibal - (wamt+0.50);
        printf("%.2f",fbal);
        }
    else(printf("%.2f",ibal));
    return 0;
    
}