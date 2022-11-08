a,b=map(int,input().split())
s=0
for i in range(a):
    s+=sum(list(map(int,input().split())))
print(s)