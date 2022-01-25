# for _ in range(int(input())):
#     n=int(input())
#     lst=[int(x) for x in input().split()]
#     print(lst[0]&lst[1],end=" ")
#     for i in range(1,len(lst)-1):
#         print(max(lst[i]&lst[i+1],lst[i]&lst[i-1]),end=" ")
#     print(lst[n-1]&lst[n-2])

class Solution(object):
    def minimumCost(self, cost):
        sumi=0
        if(len(cost)>2):
            for i in range(len(cost),0,-3):
                sumi+=cost.pop(i)
        sumi+=sum(cost)
        return sumi
print(Solution.minimumCost([6,5,7,9,2,2]))
                


       


    