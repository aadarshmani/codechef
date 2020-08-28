#include<stdio.h>
int main()
{	int t,n;
	scanf("%d", &t);
	for(int i=0;i<t;i++){
		scanf("%d", &n);
		char str[(2*n)];
		scanf("%s", str);
		int a=0,b=0,la=n,lb=n;; 
		int ans=-1;
		for(int j=0;j<2*n;j++){
			
			
			if(j % 2 == 0){
                a += (str[j] - 48);
                la--;
            }else{
                b += (str[j] - 48);
                lb--;
            }
			if(a>b+lb || b>a+la) {
                ans = j+1;
                break;
            }
			
		}
		if(ans==-1)
		{ans=2*n;}
		
		printf("%d\n", ans);
	}
	return 0;
}