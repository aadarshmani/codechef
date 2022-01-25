t=int(input())
for _ in range(t):
    m,x=map(int,input().split())
    lst=[k for k in range(x+1)]
    for i in range(2,x+1):
        calc=m%i
        if(calc==0):
            calc=i
        lst[i]=lst[i-1]
        if(lst[i]>=calc):
            lst[i]+=1
    lst.pop(0)
    print(*lst)
