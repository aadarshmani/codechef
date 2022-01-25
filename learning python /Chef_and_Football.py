from itertools import count
n=int(input())
plst=[0 for x in range(n+1)]
glst=[0 for x in range(n+1)]
for i in range(n*(n-1)//2):
    t1,t2,g1,g2=map(int,input().split())
    if(g1>g2):
        plst[t1]+=1
        glst[t1]+=g1
        glst[t2]+=g2
    elif(g2>g1):
        plst[t2]+=1
        glst[t2]+=g2
        glst[t1]+=g1
    else:
        plst[t2]+=0.5
        plst[t1]+=0.5
        glst[t2]+=g2
        glst[t1]+=g1
indices = [ind for ind, 
           ele in zip(count(),
                      plst) if ele == max(plst)]

maxi=0
pos=0
for j in indices:
    if(glst[j]>maxi):
        pos=j
        maxi=glst[j]
print(pos)
    
    




