t=int(input())
for _ in range(t):
    k=int(input())
    count=0
    while(k%2==0):
            count+=1
            k//=2
    print(count)