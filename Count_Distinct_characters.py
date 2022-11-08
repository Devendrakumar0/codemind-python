s=input()
s=s.casefold()
a=[]
for i in s:
    if(i!=" "):
        if(i not in a):
            a.append(i)
print(len(a))