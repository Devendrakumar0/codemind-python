n=input()
l=list(map(int,input().split()))
a=[]
for i in l:
    b=str(abs(i))
    a.append(len(b))
print(*a)