sum=(input())
while(sum!=sum[::-1]):
    sum=int(sum)+int(sum[::-1])
    sum=str(sum)
print(sum)
