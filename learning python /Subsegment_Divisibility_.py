for _ in range(int(input())):
    n=int(input())
    lst=[]
    for i in range(1,2000):
        if(i%4==0 or i%3==0):
            pass
        else:
            lst.append(i)
        if(len(lst)==n):
            break
    print(*lst)
        