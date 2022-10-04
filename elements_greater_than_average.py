n=int(input())
li=list(map(int,input().split()))
c=0
avg=(sum(li)//n)
for i in li:
    if avg<=i:
        c+=1
print(c)