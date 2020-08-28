#include <stdio.h>
#include <limits.h>
int main(){
	int t,n;
	scanf("%d",&t);
	for(int j=0;j<t;j++){
		scanf("%d",&n);
		 int temp=0;
		 int small= INT_MAX;
		 long long int sum=0;
		for( int i=0;i<n;i++){
			scanf("%d", &temp);
			if(temp<small){
				small=temp;
			}
			sum+=small;
			
		}
		printf("%lld\n", sum);
	}
	return 0;
}