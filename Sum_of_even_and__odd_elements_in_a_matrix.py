a,b=map(int,input().split())
e=0
o=0
for i in range(a):
    for j in (list(map(int,input().split()))):
        if(j%2==0):
            e+=j
        else:
            o+=j
print(e,o)