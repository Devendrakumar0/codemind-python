n=int(input())
li=list(map(int,input().split()))
res = []
for i in li: 
    if i not in res: 
        res.append(i) 
for i in res: 
    print(i,end=" ")