n=int(input())
li=list(map(int,input().split()))
s=s1=0
for i in li:
    if 0<=i<=9:
        s=s+i
    else:
        i=str(i)
        for j in i:
            s1=s1+int(j)
print(s+s1)
    