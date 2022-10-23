n=int(input())
s1=0
s2=0
for i in range(n):
    l=list(map(int,input().split()))
    s1+=l[i]
    s2+=l[n-i-1]
print("Principal Diagonal:%d"%s1)
print("Secondary Diagonal:%d"%s2)