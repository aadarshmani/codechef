# import math
# def Log2(x):
#     if x == 0:
#         return False
 
#     return (math.log10(x) /
#             math.log10(2))
 
# def isPowerOfTwo(n):
#     return (math.ceil(Log2(n))==math.floor(Log2(n)))

# t=int(input())
# for i in range(t):
#     n,k=map(int,input().split())
#     lst=list(range(1,n+1))
#     lst1=lst
#     if isPowerOfTwo(n):
#         ran=k%(math.ceil(Log2(n)))
#         for i in range(ran):
#             lst=lst[::2]+lst[1::2]

#     else: 
#         passes=0
#         for i in range(0,n,2):
#             lst=lst[::2]+lst[1::2]
#             lst=lst[::2]+lst[1::2]
#             passes+=2
#             if lst==lst1:
#                 break 
#         passes=k%passes

#         for i in range(passes):
#             lst=lst[::2]+lst[1::2] 

#     print(*lst)
A=int(input())
count=0
while A & 1!=1:
    count+=1
    A=A>>1
print(count)