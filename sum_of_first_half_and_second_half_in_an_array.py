n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in range(n):
    if(i<int(n/2)):
        a+=l[i]
    else:
        b+=l[i]
print(a)
print(b)