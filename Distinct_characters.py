s=input()
s=s.casefold()
a=[]
for i in s:
    if(i!=" "):
        if(i not in a):
            a.append(i)
a=sorted(a)
[print(i,end="")for i in a]
