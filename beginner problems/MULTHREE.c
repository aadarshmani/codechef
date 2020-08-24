#include<stdio.h>
#include<string.h>
int main(){
	int t;
	
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int d0,d1,temp=0;
		long long int k=0,sum=0;
		scanf("%lld%d%d",&k,&d0,&d1);
		sum=d1+d0;
		if(k<3) {
			printf("%s", (sum%3==0)?"YES":"NO");
			break;
		}
		else{
			for(int j=0;j<k-2;j++){
				temp=((d0+d1)%10);
				d0=d1;
				d1=temp;
				sum+=d1;
			}
		}
		printf("%s", (sum%3==0)?"YES":"NO");
	}
	return 0;
}