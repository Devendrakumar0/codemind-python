a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    a=abs(i)
    a=str(a)
    if(b==len(a)):
        c+=1
print(c)