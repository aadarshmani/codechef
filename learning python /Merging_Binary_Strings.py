t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    b=input()
    c=[]
    for i in range(2*n):
        
        if(a[0]=='0' and b[0]=='1'):
            c.append(a[0])
            a=a[1:]
        elif(a[0]=='1' and b[0]=='0'):
            c.append(b[0])
            b=b[1:]
        else:
            if a.count('0')>b.count('0'):
                c.append(a[0])
                a=a[1:]
            else:
                c.append(b[0])
                b=b[1:]  
        if(len(a)==0 or len(b)==0):
            c=c+list(a)+list(b)
            break   
    invs=ones=0
    for i in ''.join(c):
        if i =='1': ones +=1
        else: invs +=ones 
    print(invs)