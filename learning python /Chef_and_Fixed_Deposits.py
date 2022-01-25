t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    lst=[int(i) for i in input().split()]
    lst.sort(reverse=True)
    j,sum=0,0
    while(sum<x and j<n):
        sum+=lst[j]
        j+=1
    if(sum<x) and (j>=n):
        print("-1")
    else:
        print(j)
