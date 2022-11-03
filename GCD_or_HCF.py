a,b=map(int,input().split())
li=[]
c=0
for i in range(1,a+1):
    if a%i==0:
        li.append(i)
for j in range(1,b+1):
    if b%j==0:
        if j in li:
            c=j
print(c)