n=int(input())
li=list(map(int,input().split()))
avg=(sum(li))//n
c=0
for i in li:
    if avg==i:
        c+=1
if c>=1:
    print("True")
else:
    print("False")
        

