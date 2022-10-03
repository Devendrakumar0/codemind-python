n=int(input())
li=list(map(int,input().split()))
k=int(input())
c=0
for i in li:
    if i==k:
        c+=1
if c>=1:
    print("True")
else:
    print("False")