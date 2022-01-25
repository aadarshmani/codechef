for _ in range(int(input())):
    n,m,k=map(int,input().split())
    mlst=[int(x) for x in input().split()]
    klst=[int(x) for x in input().split()]
    flst=set([x for x in range(1,n+1)])
    ulst=[value for value in mlst if value in klst]
    combined=set(mlst+klst)
    final=flst-combined
    print(len(ulst),end=" ")
    print(len(final))


