n=int(input())
l=list(map(int,input().split()))
a=int(input())
c=0
for i in range(a):
    c+=l[i]
print(c)