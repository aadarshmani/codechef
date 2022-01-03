t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    sum1=0
    ab=list(map(int,input().split()))
    sum1=sum(ab)
    if k-sum1>-1:
        print("Yes")
    else:
        print("No")


