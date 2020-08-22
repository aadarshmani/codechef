#include<stdio.h>
#include<stdlib.h>
int cmpfunc (const void * a, const void * b)
{
    if( *(long long int*)a - *(long long int*)b < 0 )
        return -1;
    if( *(long long int*)a - *(long long int*)b > 0 )
        return 1;
    return 0;
}

int main()
{ int temp,n;
	scanf("%d",&n);
	long long int arr[n];
	for(int i=0;i<n;i++){
		scanf("%lld", &arr[i]);
		
	}
	temp = n;
	qsort(arr,n,sizeof(long long int),cmpfunc);
	long long int max=0;
	long long sales=0;
	for(long long int i=0;i<n;i++){
		sales = arr[i] * (n - i);
	    if(sales > max){
	        max = sales;
		}
	}
	
	printf("%lld", max);
	return 0;

}