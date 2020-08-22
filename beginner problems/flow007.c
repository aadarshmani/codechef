#include<stdio.h>
int main()
{
	long int n,i,temp=0,rnum;
	scanf("%ld", &n);
	for(i=0;i<n;i++)
	{	rnum=0;
		scanf("%ld", &temp);
		while((temp)>0)
		{
			rnum=(rnum*10)+(temp%10);
			temp=temp/10;
		}
		printf("%ld\n", rnum);

	}
	return 0;
}

