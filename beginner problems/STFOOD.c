#include<stdio.h>
int main()
{ 
	int t,n;
	scanf("%d", &t);
	for( int i=0;i<t;i++){
		scanf("%d", &n);
		long int sum,big=0;
		for(int j=0;j<n;j++){
			int s=0,p=0,v=0;
			scanf("%d %d %d", &s,&p,&v);
			sum=(p/(s+1))*v;
			if(big<sum)
			big=sum;
		}
		
		printf("%ld\n", big);
	}
	
	
	return 0;
}
