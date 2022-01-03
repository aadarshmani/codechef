t=int(input())
for i in range(t):
    x,y,k,n=map(int,input().split())
    flag=0
    for j in range(n):
        p,c=map(int,input().split())
        if(p-(x-y)>=0 and k>=c):
                flag+=1
        else:
            flag+=0
    if(flag==0):
        print("UnluckyChef")
    else:
        print("LuckyChef")
