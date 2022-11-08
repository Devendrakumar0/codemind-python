a,b=map(int,input().split())
c=[]
for i in range(a):
    l=list(map(int,input().split()))
    c.append(sum(l))
print(max(c))