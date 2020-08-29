#include<stdio.h>
#include<stdlib.h>
	int main(){
	long int t=0,n=0;
	scanf("%ld", &t);
	while(t--){
		scanf("%ld",&n);
		long int temp=0,a[10001]={0};
		for(long int i=0;i<n;i++){
			scanf("%ld",&temp);
			a[temp]++;
		}
		long int arr[10001]={0};
		for(long int j=1;j<10001;j++){
			if(a[j]==0){
				arr[a[j]]=-1;
			}
			else{
				arr[a[j]]++;
			}
		}
		long int big=0,pos=0;
		for (long int k = 1; k < 10001; k++) {
			if (big < arr[k]){
				big = arr[k];
				pos=k;
			}
		}	
			
		
		printf("%ld\n",pos);		
		
	}
	return 0;
}