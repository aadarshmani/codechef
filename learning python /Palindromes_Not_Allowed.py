for _ in range(int(input())):
    n=int(input())
    stri=['0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    j=1
    for i in range(1,n+1):
        ch=stri[j]
        j+=1
        print(ch,end="")
        if(j==25):
            j=1
    print("")
    
