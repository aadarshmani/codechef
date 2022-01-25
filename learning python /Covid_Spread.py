N = 1000000007

# Function code 
def exponentiation(bas, exp):
    if (exp == 0):
        return 1
    if (exp == 1):
        return bas % N

    t = exponentiation(bas, int(exp / 2))
    t = (t * t) % N

    # if exponent is
    # even value
    if (exp % 2 == 0):
        return t

    # if exponent is
    # odd value
    else:
        return ((bas % N) * t) % N

t=int(input())
for i in range(t):
    n,d=map(int,input().split())
    if  d<11:
        ans=1<<d

    else:
        x=exponentiation(3,d-10)
        ans=1024*x

    if ans>n:
        ans=n

    print(ans)