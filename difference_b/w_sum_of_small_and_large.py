n=input()
l=list(n.split())
a=[]
b=[]
for i in l:
    mi=i[0]
    ma=i[0]
    for j in i:
        if(ord(j)<ord(mi)):
            mi=j
        if(ord(j)>ord(ma)):
            ma=j
    a.append(mi)
    b.append(ma)
c=0
d=0
for i in a:
    c+=ord(i)
for i in b:
    d+=ord(i)
print(abs(c-d))