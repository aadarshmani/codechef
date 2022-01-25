def lis(arr):
    n = len(arr)
  
    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1]*n
  
    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
  
    # Initialize maximum to 0 to get
    # the maximum of all LIS
    maximum = 0
  
    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])
  
    return maximum

for _ in range(int(input())):
    lena,lenb=map(int,input().split())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    print(lis(a)+lis(b))



























    # j=0
    # temp=0
    # flag=0
    # for i in range(lena+lenb):
    #     if(temp<=a[0] and temp<=b[0]):
    #         if(a[0]<b[0]):
    #             final.append(a[0])
    #             a.pop(0)
            
    #         else:
    #             final.append(b[0])
    #             b.pop(0)
            
    #     elif(temp<=a[0] and temp>b[0]):
    #         final.append(a[0])
    #         a.pop(0)
            
    #     elif(temp<=b[0] and temp>a[0]):
    #         final.append(b[0])
    #         b.pop(0)
            
    #     else:
    #         break
    #     if len(a)==0 or len(b)==0:
    #         flag=1
    #         j=i
    #         break
            
    # if flag==1:
    #     final+= a+b
    #     for i in range(j+1,)


    
        

