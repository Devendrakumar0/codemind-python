n=int(input())
l=list(map(int,input().split()))
d=[]
c=0
for i in l:
    if(i%2==1 and i not in d):
        d.append(i)
        c+=1
print(c)