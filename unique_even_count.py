n=int(input())
li=list(map(int,input().split()))
c=0
li=set(li)
for i in li:
    if i%2==0:
        c+=1
print(c)