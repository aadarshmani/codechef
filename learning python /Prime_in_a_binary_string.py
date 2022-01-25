t=int(input())
for i in range(t):
    string=input()
    flag=0
    if len(string)==1:
        print("No")
    else:
        cnt=string.count("10")+string.count("11")
        if cnt>0:
            print("Yes")
        else:
            print("No")
