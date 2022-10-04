n=int(input())
li=list(map(int,input().split()))
c=0
for i in li:
    if i==1 or i==0:
        c+=1
if c==n:
    print("True")
else:
    print("False")