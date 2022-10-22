n=int(input())
li=list(map(int,input().split()))
c=c1=0
for i in li:
    if i%2!=0:
        c+=1
    else:
        c1+=1
print(c1,c)