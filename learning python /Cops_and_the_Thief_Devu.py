t=int(input())
for i in range(t):
    m,x,y=map(int,input().split())
    lst1=[0 for x in range(100)]
    count=0
    lst=list(map(int,input().split()))
    temp=x*y
    for k in range(m):
        mini=lst[k]-temp
        maxi=lst[k]+temp
        if(mini<1):
            mini=1
        if(maxi>100):
            maxi=100
        for l in range(mini,maxi+1):
            lst1[l-1]=1
    for q in range(len(lst1)):
        if(lst1[q]==0):
            count+=1
    print(count)