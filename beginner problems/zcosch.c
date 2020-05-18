#include <stdio.h>

int main(void) {
	// your code goes here
	int R;
	scanf("%d",&R);
	if(R<101 && R>50){
	    printf("50");
	}
	else if(R>0 && R<51){printf("100");}
	else{printf("0");}
	return 0;
}

