a,b=map(int,input().split())
e=0
o=0
for i in range(a):
    if(i%2==0):
        e+=sum(list(map(int,input().split())))
    else:
        o+=sum(list(map(int,input().split())))
print(e,o)