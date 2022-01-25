from collections import deque

n=int(input())
number_stack=deque([])
name_stack=deque([])
for i in range(n):
    a=[x for x in input().split()]
    print(a)
    
    if a[0]!='-1':
        number_stack.appendleft(a[0])
        name_stack.appendleft(a[1])
    else:
        #print("pop mode")
        count=0
        x=[int(i) for i in number_stack]
        book=min(x)
        book=str(book)
        while(book!=number_stack[0]):
            number_stack.popleft()
            name_stack.popleft()
            count+=1  
        number_stack.popleft()
        #print(number_stack,name_stack)
        print(count,end=" ")
        print(name_stack.popleft())