import itertools
t=int(input())
for i in range(t):
    n=int(input())
    lst=input()
    tup=[0 for x in range(10000)]
    for j in range(1,n):
        tup[n]=itertools.combinations(lst,n)
    print(tup)