t=int(input())
while(t>0):
    n=int(input())
    ar=list(map(int,input().split()))
    sum1=sum(ar)
    min1=min(ar)
    print(sum1-n*min1) 
    t=t-1

    


