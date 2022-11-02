a,b=map(int,input().split())
l1=[0]*b
for i in range(a):
    l=list(map(int,input().split()))
    for i in range(b):
        if(l1[i]<l[i]):
            l1[i]=l[i]
for i in l1:
    print(i)