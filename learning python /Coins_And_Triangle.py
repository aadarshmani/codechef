t=int(input())
for _ in range(t):
    n=int(input())
    i=1
    sums=0
    count=0
    while(n>sums):
        sums+=i
        count+=1
        i+=1
    print(count)

