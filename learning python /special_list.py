n=int(input())
lst=[0 for x in range(n)]
dif=[]
for i in range(n):
    lst[i]=int(input())
for i in range(n-1):
    x=lst[i+1]-lst[i]
    dif.append(x)
count=0
for k in range(len(dif)-1):
    if(dif[k+1]>dif[k]):
        count+=1
print(count)
