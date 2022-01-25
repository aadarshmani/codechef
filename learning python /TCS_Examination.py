t=int(input())
for _ in range(t):
    t1=tuple(int(i) for i in input().split())
    t2=tuple(int(i) for i in input().split())
    if t1==t2:
        print("TIE")
    else:
        if sum(t1)==sum(t2):
            if t1[0]==t2[0]:
                print("DRAGON") if t1[1]>t2[1] else print("SLOTH")
            else:
                print("DRAGON") if t1[0]>t2[0] else print("SLOTH")
        else:
             print("DRAGON") if sum(t1)>sum(t2) else print("SLOTH")