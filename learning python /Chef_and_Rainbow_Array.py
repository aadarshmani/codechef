t=int(input())
for i in range(t):
    n=int(input())
    ar=list(map(int,input().split()))
    list1=[0,0,0,0,0,0,0,0]
    nlist=[]
    for j in range(n):
        if(ar[j]<8 and ar[j]>0):
            list1[ar[j]]+=1
    list1//=2
    for k in range(7):
        for l in range(list1[k]):
            nlist.append(i)
        