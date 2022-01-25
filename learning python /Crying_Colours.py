t=int(input())
for i in range(t):
    ans=[]
    n=int(input())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))    
    lst3=list(map(int,input().split()))
    print(max(lst1[1]+lst1[2]+lst2[2],lst2[0]+lst3[0]+lst3[1]))