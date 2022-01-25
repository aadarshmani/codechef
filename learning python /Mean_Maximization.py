for _ in range(int(input())):
    n=int(input())
    lst=[int(x) for x in input().split()]
    maxi=max(lst)
    lst.pop(lst.index(max(lst)))
    print(maxi+(sum(lst)/len(lst)))
   