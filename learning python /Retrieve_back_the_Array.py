t = int(input())
for i in range(t):
    n, x = (map(int, input().split()))
    lst = []
    count = 0
    if(n == 1):
        lst.append(x)
    else:
        for j in range(0, 10**5):
            if x ^ j not in lst:
                x = x ^ j
                lst.append(j)
                count += 1
            if count == n-1:
                lst.append(x)
                break
    print(*lst)
