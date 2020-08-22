#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
	char *ptr;int T,l;
	ptr = (char*) calloc(1024,(sizeof(char)));
	int a[26]={},flag;
	scanf("%d", &T);
	for(int i=0;i<T;i++){
		scanf("%s",ptr);
		int a[26]={},flag;
		l=strlen(ptr);
		for(int i=0, j=l-1;i<j;i++,j--){
			a[ptr[i]-'a']++;
		    a[ptr[j]-'a']--;

		}
		if(l==1){
			flag=1;
		}
		if(l>1){
			for(int k=0;k<26;k++){
				if(a[k]!=0)
				{
					flag=0;break;
				}
				else
				{
					flag=1;

				}
			}
			flag==0?printf("NO\n"): printf("YES\n");
		}
		else{
			printf("NO");
		}
		
	}
	free(ptr);
return 0;
	 
}