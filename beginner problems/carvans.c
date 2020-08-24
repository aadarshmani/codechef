#include<stdio.h>
#include<limits.h>
int main(){
	int t,n;
	scanf("%d", &t);
	for(int i=0;i<t;i++)
	{
		scanf("%d", &n);
		int pre=INT_MAX,ele,count=0;
		for(int j=0;j<n;j++){
			scanf("%d", &ele);
			if(pre>=ele){
				count++;
				pre=ele;
			}
		}
		printf("%d\n", count);
	}
	return 0;

}