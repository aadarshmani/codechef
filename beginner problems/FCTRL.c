#include<stdio.h>
int main()
{	
	long long int n, num;
	scanf("%lld", &n);
	for(int i=0;i<n;i++)
	{	long long int fact=1,count=0;
		scanf("%lld", &num);
		for(int i=2;i<num+1;i++)
		{
			fact=fact*i;
		}
		while((fact%10)==0)
		{
			count++;
			fact=fact/10;
		}
		printf("%lld\n", count);
		
	}
	return 0;
}