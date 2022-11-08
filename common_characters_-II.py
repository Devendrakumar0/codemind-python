s1=input()
s2=input()
s1=s1.casefold()
s2=s2.casefold()
a=[]
for i in s1:
    if(i!=" "):
        if(i in s2)and(i not in a):
            a.append(i)
print(len(a))