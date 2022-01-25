t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    lst=input()
    seti=set(lst)
    lst1=list(seti)
    ans=c-len(lst1)
    if(ans<1):
        print(0)
    else:
        print(ans)