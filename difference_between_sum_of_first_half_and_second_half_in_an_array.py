n=int(input())
l=list(map(int,input().split()))
a=0
b=0
if(n%2!=0):
    l.append(l[n-1]+1)
    n=n+1
for i in range(n):
    if(i<int(n/2)):
        a+=i
    else:
        b+=i
print(abs(a-b))