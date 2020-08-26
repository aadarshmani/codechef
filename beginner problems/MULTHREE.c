#include<stdio.h>
#include<string.h>
int main(){
	int t;
	
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int d0,d1,temp=0;
		long long int k=0,sum=0,ans;
		scanf("%lld%d%d",&k,&d0,&d1);
		temp=d1+d0;
		ans=temp;
		sum=(2*temp) % 10 + (4*temp) % 10 + (8*temp) % 10 + (6*temp) % 10;
		k -= 2;

	if(k > 0) {
		ans += (temp % 10);
		k--;
	}

	ans += (k / 4) * sum;

	k %= 4;

	int p = 2;
	while(k--) {
		ans += (p*temp) % 10;
		p = (p * 2) % 10;
	}

		if((ans % 3) == 0)
		printf("YES\n");
		else
		printf("NO\n");
	}
	return 0;
}