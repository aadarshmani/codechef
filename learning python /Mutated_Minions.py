t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    ar=list(map(int,input().split()))
    nar=[x+k for x in ar]
    count=0
    for j in range(n):
        if(nar[j]%7==0):
            count+=1
    print(count)
    print("\n")
