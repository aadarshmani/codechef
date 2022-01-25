t = int(input())
for i in range(t):
    n, a = map(int, input().split())
    nflag = n & 1
    aflag = a & 1
    if(n == 1):
        if aflag == 1:
            print("Odd")
        else:
            print("Even")
    elif aflag == 1:
        if nflag == 0:
            print("Even")
        else:
            print("Odd")
    else:
        if(nflag == 0 and aflag == 0):
            print("Impossible")
        elif(nflag == 1 and aflag == 0):
            print("Impossible")
