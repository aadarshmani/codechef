def next(arr, target):
    start = 0
    end = len(arr) - 1
 
    ans = -1
    while (start <= end):
        mid = (start + end) // 2
 
        # Move to right side if target is
        # greater.
        if (arr[mid] <= target):
            start = mid + 1
 
        # Move left side.
        else:
            ans = mid
            end = mid - 1
 
    return ans


t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    slst = list()
    for i in range(len(lst)):
        flag = 0
        if len(slst) == 0:
            slst.append(lst[i])
            continue

        else:
            if next(slst,lst[i])==len(slst):
                slst.append(lst[i])
            else:
                if(slst[next(slst,lst[i])] > lst[i]):
                    slst[next(slst,lst[i])] = lst[i]
                    flag = 0
                    break
                else:
                    if(slst[i-1] < lst[i]):
                        slst.append(lst[i])
                    else:
                        slst = lst[i]+slst

    print(len(slst), end=" ")
    print(*slst)
