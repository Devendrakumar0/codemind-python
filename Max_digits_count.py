n=input()
l=list(map(int,input().split()))
b=[]
for i in l:
    a=str(abs(i))
    b.append(len(a))
print(b.count(max(b)))