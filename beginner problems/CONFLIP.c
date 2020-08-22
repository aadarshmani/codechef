#include<stdio.h>
int main()
{
	int T,G,I,N,Q;
	scanf("%d", &T);
	for(int i=0; i<T; i++){
		scanf("%d", &G);
		for(int j=0;j<G;j++)
		{
			scanf("%d %d %d" , &I, &N, &Q);
			if(I==1)
			{
				if(N%2==1)
				{
					if(Q%2==1)
					{
						printf("%d\n", N/2);
					}
					else
					{
						printf("%d\n", (N/2)+1);
					}
				}
				else
				{
					printf("%d\n", N/2);
				}
			}
			else
			{
				if(N%2==1)
				{
					if(Q%2==1)
					{
						printf("%d\n", (N/2)+1);
					}
					else
					{
						printf("%d\n", (N/2));
					}
				}
				else
				{
					printf("%d\n", N/2);
				}
			}		
		}
	}
	return 0;
}