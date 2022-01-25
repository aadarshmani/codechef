t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    strlst1=[]
    strlst2=[]
    strlst1=list(map(str,input().split()))
    for x in range(k):
        strlst2=list(map(str,input().split()))
        strlst2.remove(strlst2[0])         
        for j in range(len(strlst1)):
            if strlst1[j] in strlst2:
                strlst1[j]="YES"
    for i in range(len(strlst1)):
        if strlst1[i]=="YES":
            pass
        else:
            strlst1[i]="NO"
    for i in strlst1:
        print(i,end=" ")
    print("")
