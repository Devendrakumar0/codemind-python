s1=input()
s1=s1.casefold()
l1=list(s1.split())
a=[]
for i in l1[0]:
    for j in l1[1::]:
        if(i not in j):
            break
    else:
        a.append(i)
if(len(a)==0):
    print(-1)
else:
    [print(i,end="") for i in a]