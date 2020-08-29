#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	short int t;
	scanf("%hd",&t);
	while(t--){
		char* str;
		str=(char*)malloc(10000000*sizeof(char));
		scanf("%s%*c", str);
		//printf(" %s", str);
		int len=0,o=0,i;
		//printf(" %lu",strlen(str));
		for(i=0;i<strlen(str);i++){
			if(str[i]==62){
				o--;
				//printf(" %d",o);
			}
			else if(str[i]==60){
				o++;
				//printf(" %d",o);
			}
			if(o==0)len=i+1;
			if(o<0||i==strlen(str)-1){
				printf("%d\n", len);
				break;
			}
		}
		free(str);
			
			
	}
	return 0;
}