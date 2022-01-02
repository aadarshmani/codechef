#include <stdio.h>
#include <math.h>
int result(long int num) 
	{	
		int ctr = 0;
		for(int i=1; i<=sqrt(num); i++)
	    {
	        if(num%i==0 && i*i!=num)
	        {
	            ctr+=2;
	        } 
	        else if (i*i==num) 
	        {
	            ctr++;
	        }
	    }
	        return ctr;
	}
int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        long int n, ans, count = 0;
        scanf("%ld", &n);
        n=n-1;
        ans=result(n);
        printf("%ld\n", ans);
    }
    return 0;
}
