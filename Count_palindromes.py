n=int(input())
li=list(map(int,input().split()))
c=0
for i in li:
    i=str(i)
    if i[::-1]==i:
        c+=1
print(c)