lst=input()
type1=["(","[","{"]
type2=[")","[","{"]
stac=[]
temp=0
count=0
for i in range(len(lst)):
    if lst[i] in type1:
        stac.append(lst[i])
        count+=1
    else:
        if lst[i] in type2:
            if lst[i]==stac[-1]:
                count-=1
                stac.pop(-1)
            else:
                temp=i 
                break
if(temp==0):
    print("no error")
else:
    print(temp)
        



