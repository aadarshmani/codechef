#include<stdio.h>
int main()
{	
	int n, num;
	scanf("%d", &n);
	for(int i=0;i<n;i++)
	{	int count=0;
		scanf("%d", &num);
	    for(int j=5;num/j>=1;j=j*5){
	        count+=num/j;
	    }
		printf("%d\n", count);
	}
	return 0;
}