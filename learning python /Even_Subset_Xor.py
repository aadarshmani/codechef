from itertools import count


def countSetBits(n):

    count = 0
    while (n):
        n &= (n-1) 
        count+= 1
    
    return count
t=int(input())
for _ in range(t):
    n=int(input())
    lst=[]
    for i in range(1,2**20):
        temp=countSetBits(i)
        if(temp%2==0):
            lst.append(i)
            if(len(lst)==n):
                break
        else:
            pass
    print(*lst)
